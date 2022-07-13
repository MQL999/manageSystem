"""
#-*-coding:utf-8-*-
@Project:manageSystem
@File:phonenum.py
@Author:闵麒良
@Time:2022/7/7 20:44

"""
from django.shortcuts import render,redirect
from app.models import PrettyPhoneNum
from app.utils.pagenation import pageNation
from app.utils.form import phoneModelForm,phoneEditModelForm


def phoneNum_list(request):
    """靓号列表"""
    data_dict={}
    search_data=request.GET.get("q","")
    if search_data:
        data_dict["phone_num__contains"]=search_data
    #分页
    data = PrettyPhoneNum.objects.filter(**data_dict).order_by("level")
    page_object=pageNation(request,data,search_data)
    context={
        "data": page_object.data,
        "search_data": search_data,
        "page_string": page_object.Html()
    }
    return render(request,"phonenum_list.html",context)

def phonenum_add(request):
    """添加靓号"""
    if request.method=="GET":
        form = phoneModelForm()
        return render(request, 'phonenum_add.html', {"form": form})
    else:
        form=phoneModelForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("/phonenum/list/")
        else:
            return render(request,"phonenum_add.html",{"form":form})

def phonenum_delete(request):
    id=request.GET.get("id")
    PrettyPhoneNum.objects.filter(id=id).delete()
    return redirect("/phonenum/list/")

def phonenum_edit(request,id):
    row_object=PrettyPhoneNum.objects.filter(id=id).first()
    if request.method=="GET":
        form=phoneEditModelForm(instance=row_object)
        return render(request,'phonenum_edit.html',{"form":form})
    else:
        form = phoneEditModelForm(data=request.POST,instance=row_object)
        if form.is_valid():
            form.save()
            return redirect("/phonenum/list/")
        else:
            return render(request,'phonenum_edit.html',{"form":form})

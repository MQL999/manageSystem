"""
#-*-coding:utf-8-*-
@Project:manageSystem
@File:users.py
@Author:闵麒良
@Time:2022/7/7 20:44

"""
from django.shortcuts import render,redirect
from app.models import userInfo
from app.utils.pagenation import pageNation
from app.utils.form import userModelForm


def user_list(request):
    """用户管理"""
    data_dict = {}
    search_data = request.GET.get("q", "")
    if search_data:
        data_dict["name__contains"] = search_data
    data = userInfo.objects.filter(**data_dict).order_by("age")
    page_object = pageNation(request, data,search_data)
    context={
             "data":page_object.data,
             "search_data": search_data,
             "page_string": page_object.Html()
             }
    return render(request,"user_list.html",context)

def user_add(request):
    """添加用户，使用jiango带的modelform"""
    if request.method=="GET":
        form = userModelForm()
        return render(request, "user_add.html", {"form": form})
    else:
        form=userModelForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("/user/list/")
        else:
            return render(request, "user_add.html", {"form": form})

def user_delete(request):
    """删除员工"""
    id=request.GET.get("id")
    userInfo.objects.filter(id=id).delete()
    return redirect("/user/list/")

def user_edit(request,id):
    row_object = userInfo.objects.filter(id=id).first()
    if request.method == "GET":
        form=userModelForm(instance=row_object)
        return render(request, "user_edit.html", {"form":form})
    else:
        form=userModelForm(data=request.POST,instance=row_object)
        if form.is_valid():
            form.save()
            return redirect("/user/list/")
        else:
            return render(request,"user_edit.html",{"form":form})
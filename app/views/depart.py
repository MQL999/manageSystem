"""
#-*-coding:utf-8-*-
@Project:manageSystem
@File:depart.py
@Author:闵麒良
@Time:2022/7/7 20:43

"""
from django.shortcuts import render,redirect
from app.models import departMent
from app.utils.pagenation import pageNation

def depart_list(request):
    if request.method=="GET":
        data_dict = {}
        search_data = request.GET.get("q", "")
        if search_data:
            data_dict["title__contains"] = search_data
        data = departMent.objects.filter(**data_dict).order_by("id")
        page_object = pageNation(request, data, search_data)
        context = {"data": page_object.data,
                   "search_data":search_data,
                   "page_string": page_object.Html()
                   }
        return render(request,"department.html",context)

def depart_add(request):
    if request.method=="GET":
        return render(request,"depart_add.html")
    else:
        title=request.POST.get("title")
        departMent.objects.create(title=title)
        return redirect("/depart/list/")

def depart_delete(request):
    depart_id=request.GET.get("id")
    departMent.objects.filter(id=depart_id).delete()
    return redirect("/depart/list/")

def depart_edit(request,depart_id):
    if request.method=="GET":
        data=departMent.objects.filter(id=depart_id).first()
        return render(request,"depart_edit.html",{"data":data})
    else:
        title=request.POST.get("title")
        departMent.objects.filter(id=depart_id).update(title=title)
        return redirect("/depart/list/")
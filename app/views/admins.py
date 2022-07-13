"""
#-*-coding:utf-8-*-
@Project:manageSystem
@File:admins.py
@Author:闵麒良
@Time:2022/7/8 13:25

"""
from django.shortcuts import render,redirect
from app.models import Admin
from app.utils.pagenation import pageNation
from app.utils.form import AdminModelForm,AdminEditModelForm,AdminResetModelForm

def admin_list(request):
    data_dict = {}
    search_data = request.GET.get("q", "")
    if search_data:
        data_dict["username__contains"] = search_data
    data = Admin.objects.filter(**data_dict).order_by("id")
    page_object = pageNation(request, data, search_data)
    context = {
        "data": page_object.data,
        "search_data": search_data,
        "page_string": page_object.Html()
    }
    return render(request,"admin_list.html",context)

def admin_add(request):
    """添加管理员"""
    if request.method=="GET":
        form=AdminModelForm()
        return render(request,"admin_add.html",{"form":form})
    else:
        form=AdminModelForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("/admins/list/")
        else:
            return render(request, "admin_add.html", {"form": form})

def admin_edit(request,id):
    row_object=Admin.objects.filter(id=id).first()
    if not row_object:
        return redirect("/admins/list/")

    if request.method=="GET":
        form=AdminEditModelForm(instance=row_object)
        return render(request,"admin_edit.html",{"form":form})
    else:
        form=AdminEditModelForm(data=request.POST,instance=row_object)
        if form.is_valid():
            form.save()
            return redirect("/admins/list/")
        else:
            return render(request, "admin_edit.html", {"form": form})

def admin_delete(requet,id):
    row_object = Admin.objects.filter(id=id).first()
    if not row_object:
        return redirect("/admins/list/")

    Admin.objects.filter(id=id).delete()
    return redirect("/admins/list/")

def admin_reset(request,id):
    row_object = Admin.objects.filter(id=id).first()
    if not row_object:
        return redirect("/admins/list/")

    if request.method == "GET":
        form = AdminResetModelForm()
        return render(request, "admin_reset.html", {"form": form})
    else:
        form = AdminResetModelForm(data=request.POST, instance=row_object)
        if form.is_valid():
            form.save()
            return redirect("/admins/list/")
        else:
            return render(request, "admin_reset.html", {"form": form})



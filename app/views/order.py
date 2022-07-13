"""
#-*-coding:utf-8-*-
@Project:manageSystem
@File:order.py
@Author:闵麒良
@Time:2022/7/10 14:40

"""
from django.shortcuts import render
from app.utils.form import OrderModelForm,orderEditModelForm
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from app.models import phoneNumOrder
import random
from datetime import datetime

from app.utils.pagenation import pageNation


def order_list(request):
    form=OrderModelForm()
    data_dict = {}
    search_data = request.GET.get("q", "")
    if search_data:
        data_dict["phone_num__contains"] = search_data
    # 分页
    data = phoneNumOrder.objects.filter(**data_dict).order_by("order_id")
    page_object = pageNation(request, data, search_data)
    context = {
        "data": page_object.data,
        "search_data": search_data,
        "page_string": page_object.Html(),
        "form": form
    }
    return render(request, "order_list.html",context)


@csrf_exempt
def order_add(request):
    form=OrderModelForm(data=request.POST)
    if form.is_valid():
        form.instance.order_id=datetime.now().strftime("%Y%m%d%H%M%S")+str(random.randint(1000,9999))
        form.save()
        return JsonResponse({"status":True})
    else:
        return JsonResponse({"status":False,"error":form.errors})

def order_delete(request):
    id=request.GET.get("uid")
    exists= phoneNumOrder.objects.filter(id=id).exists()
    if not exists:
        return JsonResponse({"status":False,"error":"删除失败，您所删除的订单不存在！"})
    else:
        phoneNumOrder.objects.filter(id=id).delete()
        return JsonResponse({"status":True})

def order_detail(request):
    uid=request.GET.get("uid")
    row_object=phoneNumOrder.objects.filter(id=uid).values("phone_num","price","email","status","principal_id").first()
    if not row_object:
        return JsonResponse({"status": False, "error": "不存在此订单，无法编辑！"})
    else:
        res={
            "status":True,
            "data":row_object
        }
        return JsonResponse(res)

@csrf_exempt
def order_edit(request):
    uid=request.GET.get("uid")
    row_object=phoneNumOrder.objects.filter(id=uid).first()
    form = orderEditModelForm(data=request.POST,instance=row_object)
    if form.is_valid():
        form.save()
        return JsonResponse({"status": True})
    else:
        return JsonResponse({"status": False, "error": form.errors})



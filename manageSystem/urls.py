"""manageSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import depart,users,phonenum,admins,account,order

urlpatterns = [
    #部门管理
    path('admin/', admin.site.urls),
    path('depart/list/', depart.depart_list),
    path('depart/add/',depart.depart_add),
    path('depart/delete/',depart.depart_delete),
    path('depart/<int:depart_id>/edit/',depart.depart_edit),

    #用户管理
    path('user/list/',users.user_list),
    path('user/add/', users.user_add),
    path('user/delete/', users.user_delete),
    path('user/<int:id>/edit/', users.user_edit),

    #靓号管理
    path('phonenum/list/',phonenum.phoneNum_list),
    path('phonenum/add/',phonenum.phonenum_add),
    path('phonenum/delete/',phonenum.phonenum_delete),
    path('phonenum/<int:id>/edit/',phonenum.phonenum_edit),

    #管理员
    path('admins/list/', admins.admin_list),
    path('admins/add/',admins.admin_add),
    path('admins/<int:id>/edit/',admins.admin_edit),
    path('admins/<int:id>/delete/',admins.admin_delete),
    path('admins/<int:id>/reset/',admins.admin_reset),

    #登录
    path('login/',account.login),

    #注销登录
    path('logout/',account.logout),

    #默认视图
    path('',account.index),

    #生成随机图片验证码
    path('image/code/',account.image_code),

    #订单管理
    path('order/list/',order.order_list),
    path('order/add/', order.order_add),
    path('order/delete/',order.order_delete),
    path('order/detail/',order.order_detail),
    path('order/edit/',order.order_edit)

]

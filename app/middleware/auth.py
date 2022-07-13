"""
#-*-coding:utf-8-*-
@Project:manageSystem
@File:auth.py
@Author:闵麒良
@Time:2022/7/8 21:37

"""
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect
class AuthMiddleWare(MiddlewareMixin):

    def process_request(self,request):
        if request.path_info in ["/login/","/image/code/"]:
            return

        userInfo_dict=request.session.get("userInfo")
        if userInfo_dict:
            return
        else:
            return redirect("/login/")

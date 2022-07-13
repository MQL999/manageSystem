"""
#-*-coding:utf-8-*-
@Project:manageSystem
@File:encrypt.py
@Author:闵麒良
@Time:2022/7/8 15:01

"""
from django.conf import settings
import hashlib

def md5(data_string):
    obj=hashlib.md5(settings.SECRET_KEY.encode("utf-8"))
    obj.update(data_string.encode("utf-8"))
    return obj.hexdigest()
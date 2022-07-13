"""
#-*-coding:utf-8-*-
@Project:manageSystem
@File:account.py
@Author:闵麒良
@Time:2022/7/8 17:13

"""
from app.utils.form import LoginForm
from django.shortcuts import render,redirect,HttpResponse
from app.models import Admin
from app.utils.create_code import check_code
from io import BytesIO
def login(request):
    if request.method=="GET":
        form=LoginForm()
        return render(request,"login.html",{"form":form})
    else:
        form=LoginForm(data=request.POST)
        if form.is_valid():
            user_input_code=form.cleaned_data.pop("code")
            img_code=request.session.get("image_code","")
            if user_input_code.upper() != img_code.upper():
                form.add_error("code", "验证码错误或过期！")
                return render(request, "login.html", {"form": form})
            admin_object=Admin.objects.filter(**form.cleaned_data).first()
            if not admin_object:
                form.add_error("password","用户名或密码错误！")
                return render(request, "login.html", {"form": form})
            else:
                request.session["userInfo"]={"id":admin_object.id,"username":admin_object.username}
                request.session.set_expiry(60*60*24)
                request.session.pop("image_code")
                return redirect("/admins/list/")
        else:
            return render(request,"login.html",{"form":form})

def logout(request):
    request.session.clear()
    return redirect("/login/")

def index(request):
    return redirect("/admins/list/")

def image_code(request):
    """生成图片验证码"""
    img,code_string=check_code()
    stream = BytesIO()
    img.save(stream, 'png')
    request.session["image_code"]=code_string
    request.session.set_expiry(60)
    return HttpResponse(stream.getvalue())

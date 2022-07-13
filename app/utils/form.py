"""
#-*-coding:utf-8-*-
@Project:manageSystem
@File:form.py
@Author:闵麒良
@Time:2022/7/7 20:35

"""
from django import forms
import re
from django.core.exceptions import ValidationError
from app.models import userInfo,PrettyPhoneNum,Admin,phoneNumOrder
from app.utils.encrypt import md5

class userModelForm(forms.ModelForm):
    """modelForm类"""
    class Meta:
        model=userInfo
        fields=["name","sex","age","salary","entry_time","email","depart"]
        widgets = {
            'name':forms.TextInput(attrs={"class":"form-control"}),
            'sex':forms.Select(attrs={"class":"form-control"}),
            'age': forms.NumberInput(attrs={"class": "form-control"}),
            'salary': forms.NumberInput(attrs={"class": "form-control"}),
            'entry_time': forms.TextInput(attrs={"class": "form-control"}),
            'email': forms.EmailInput(attrs={"class": "form-control"}),
            'depart': forms.Select(attrs={"class": "form-control"})
        }

    #这个添加样式的方法比较简单，但是目前出现了点BUG,占时放弃使用
    # def __init__(self,*args,**kwargs):
    #     super().__init__(*args,*kwargs)
    #     for name,field in self.fields.items():
    #         field.widget.attrs={"class":"form-control"}

class phoneModelForm(forms.ModelForm):

    class Meta:
        model=PrettyPhoneNum
        fields=["phone_num","price","level","status"]
        widgets = {
            'phone_num': forms.TextInput(attrs={"class": "form-control"}),
            'price': forms.NumberInput(attrs={"class": "form-control"}),
            'level': forms.Select(attrs={"class": "form-control"}),
            'status': forms.Select(attrs={"class": "form-control"})
        }

    def clean_phone_num(self):
        phonenum = self.cleaned_data["phone_num"]
        isExist=PrettyPhoneNum.objects.filter(phone_num=phonenum).exists()
        if re.match(r"^1[3-9]\d{9}$",phonenum) and isExist==False:
            return phonenum
        elif isExist==True:
            raise ValidationError("手机号已存在，请重新填写！")
        else:
            raise ValidationError('手机号无效，请填写正确格式的手机号')

class phoneEditModelForm(phoneModelForm):

    def clean_phone_num(self):
        phonenum = self.cleaned_data["phone_num"]
        isExist = PrettyPhoneNum.objects.exclude(id=self.instance.pk).filter(phone_num=phonenum).exists()
        if re.match(r"^1[3-9]\d{9}$",phonenum) and isExist==False:
            return phonenum
        elif isExist == True:
            raise ValidationError("手机号已存在，请重新填写！")
        else:
            raise ValidationError('手机号无效，请填写正确格式的手机号')

class AdminModelForm(forms.ModelForm):
    confirm_password=forms.CharField(label="确认密码",widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"请再次输入密码"},render_value=True))
    class Meta:
        model=Admin
        fields=["username","password","confirm_password"]
        widgets={
            "username":forms.TextInput(attrs={"class":"form-control","placeholder":"请输入用户名"}),
            "password":forms.PasswordInput(attrs={"class": "form-control","placeholder":"请输入密码"},render_value=True),
        }

    def clean_username(self):
        uname=self.cleaned_data.get("username")
        isExist = Admin.objects.filter(username=uname).exists()
        if isExist:
            raise ValidationError("管理员已存在！")
        else:
            return uname

    def clean_password(self):
        pwd = self.cleaned_data.get("password")
        return md5(pwd)

    def clean_confirm_password(self):
        pwd=self.cleaned_data.get("password")
        confirm_pwd=md5(self.cleaned_data.get("confirm_password"))
        if pwd==confirm_pwd:
            return confirm_pwd
        else:
            raise ValidationError("密码不匹配，请重新输入！")

class AdminEditModelForm(forms.ModelForm):
    class Meta:
        model=Admin
        fields=["username"]
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control", "placeholder": "请输入用户名"}),
        }

    def clean_username(self):
        uname = self.cleaned_data.get("username")
        isExist = Admin.objects.filter(username=uname).exists()
        if isExist:
            raise ValidationError("管理员已存在！")
        else:
            return uname

class AdminResetModelForm(AdminModelForm):
    class Meta:
        model=Admin
        fields=["password"]
        widgets = {
            "password": forms.PasswordInput(attrs={"class": "form-control", "placeholder": "请输入新密码"},render_value=True),
        }

    def clean_password(self):
        pwd = self.cleaned_data.get("password")
        md5_pwd=md5(pwd)
        isexist=Admin.objects.filter(id=self.instance.pk,password=md5_pwd).exists()

        if isexist:
            raise ValidationError("新密码不能和旧密码相同！")
        else:
            return md5_pwd

    def clean_confirm_password(self):
        pwd = self.cleaned_data.get("password")
        confirm_pwd = md5(self.cleaned_data.get("confirm_password"))
        if pwd == confirm_pwd:
            return confirm_pwd
        elif pwd==None:
            raise ValidationError("")
        else:
            raise ValidationError("密码不匹配，请重新输入！")

class LoginForm(forms.Form):
    username=forms.CharField(label="用户名",
                             widget=forms.TextInput(attrs={"class":"form-control","placeholder":"用户名"}),
                             required=True
                             )
    password=forms.CharField(label="密码",
                             widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"密码"},render_value=True),
                             required=True,
                             )
    code=forms.CharField(
        label="验证码",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "请输入验证码"}),
        required=True,
    )
    def clean_password(self):
        pwd=self.cleaned_data.get("password")
        return md5(pwd)

class OrderModelForm(forms.ModelForm):
    class Meta:
        model=phoneNumOrder
        exclude=["order_id"]
        widgets={
            "phone_num": forms.TextInput(attrs={"class": "form-control"}),
            "price": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.TextInput(attrs={"class": "form-control"}),
            "status": forms.Select(attrs={"class": "form-control"}),
            "principal_id": forms.Select(attrs={"class": "form-control"})
        }

    def clean_phone_num(self):
        phone_num=self.cleaned_data.get("phone_num")
        exists=phoneNumOrder.objects.filter(phone_num=phone_num).exists()
        if exists:
            raise ValidationError("此靓号已经售出！")
        elif not re.match(r"^1[3-9]\d{9}$",phone_num):
            raise ValidationError("此靓号不存在！")
        else:
            return phone_num

class orderEditModelForm(OrderModelForm):
    def clean_phone_num(self):
        phone_num=self.cleaned_data.get("phone_num")
        exists=phoneNumOrder.objects.exclude(id=self.instance.pk).filter(phone_num=phone_num).exists()
        if exists:
            raise ValidationError("此靓号已在其他订单中！")
        elif not re.match(r"^1[3-9]\d{9}$",phone_num):
            raise ValidationError("此靓号不存在！")
        else:
            return phone_num




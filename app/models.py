from django.db import models

class departMent(models.Model):
    """部门表"""
    title=models.CharField(verbose_name="部门名称",max_length=32)

    def __str__(self):
        return self.title

class userInfo(models.Model):
    """员工信息表"""
    sex_choice=(
        (1,"男"),
        (2,"女")
    )
    name=models.CharField(verbose_name="姓名",max_length=16)
    sex=models.SmallIntegerField(verbose_name="性别",choices=sex_choice)
    age=models.IntegerField(verbose_name="年龄")
    salary=models.DecimalField(verbose_name="薪资",max_digits=10,decimal_places=2,default=0)
    entry_time=models.DateField(verbose_name="入职时间")
    depart=models.ForeignKey(to="departMent",to_field="id",on_delete=models.CASCADE,verbose_name="部门")
    email=models.EmailField(verbose_name="邮箱")

class PrettyPhoneNum(models.Model):
    """靓号表"""
    phone_num=models.CharField(verbose_name="手机号",max_length=11)
    price=models.IntegerField(verbose_name="价格",default=0)
    level_choice=(
        (1,"一级"),
        (2, "二级"),
        (3, "三级"),
        (4, "四级")
    )
    level=models.SmallIntegerField(verbose_name="级别",choices=level_choice,default=1)

    status_choice=(
        (1,"已占用"),
        (2,"未占用")
    )
    status=models.SmallIntegerField(verbose_name="状态",choices=status_choice,default=2)

class Admin(models.Model):
    username=models.CharField(verbose_name="用户名",max_length=32)
    password=models.CharField(verbose_name="密码",max_length=64)
    def __str__(self):
        return self.username

class phoneNumOrder(models.Model):
    order_id=models.CharField(verbose_name="订单号",max_length=64)
    phone_num=models.CharField(verbose_name="商品名",max_length=11)
    price=models.IntegerField(verbose_name="价格")
    email=models.EmailField(verbose_name="购买者邮箱")
    status_choice=(
        (1,"待支付"),
        (2,"已支付")
    )
    status=models.SmallIntegerField(verbose_name="状态",choices=status_choice,default=1)
    principal_id=models.ForeignKey(to="Admin",to_field="id",on_delete=models.CASCADE,verbose_name="订单负者人")

###  一、项目简介

本项目是一个基于django web框架的管理系统，涉及bootstrap框架，ajax，jquery，mysql以及前端基本技术。

项目文件结构：

~~~
D:.
│  manage.py
│
├─.idea
│  │  .gitignore
│  │  dbnavigator.xml
│  │  manageSystem.iml
│  │  misc.xml
│  │  modules.xml
│  │  workspace.xml
│  │
│  ├─inspectionProfiles
│  │      profiles_settings.xml
│  │      Project_Default.xml
│  │
│  └─ZeppelinRemoteNotebooks
├─app
│  │  admin.py
│  │  apps.py
│  │  models.py
│  │  tests.py
│  │  __init__.py
│  │
│  ├─middleware
│  │  │  auth.py
│  │  │
│  │  └─__pycache__
│  │          auth.cpython-38.pyc
│  │
│  ├─migrations
│  │  │  0001_initial.py
│  │  │  0002_prettyphonenum_alter_userinfo_depart.py
│  │  │  0003_admin.py
│  │  │  0004_phonenumorder.py
│  │  │  0005_rename_sratus_phonenumorder_status.py
│  │  │  __init__.py
│  │  │
│  │  └─__pycache__
│  │          0001_initial.cpython-38.pyc
│  │          0002_prettyphonenum_alter_userinfo_depart.cpython-38.pyc
│  │          0003_admin.cpython-38.pyc
│  │          0004_phonenumorder.cpython-38.pyc
│  │          0005_rename_sratus_phonenumorder_status.cpython-38.pyc
│  │          __init__.cpython-38.pyc
│  │
│  ├─static
│  │  ├─css
│  │  │      bootstrap-datetimepicker.min.css
│  │  │      bootstrap-theme.css
│  │  │      bootstrap-theme.css.map
│  │  │      bootstrap-theme.min.css
│  │  │      bootstrap-theme.min.css.map
│  │  │      bootstrap.css
│  │  │      bootstrap.css.map
│  │  │      bootstrap.min.css
│  │  │      bootstrap.min.css.map
│  │  │
│  │  ├─fonts
│  │  │      framdit.ttf
│  │  │      glyphicons-halflings-regular.eot
│  │  │      glyphicons-halflings-regular.svg
│  │  │      glyphicons-halflings-regular.ttf
│  │  │      glyphicons-halflings-regular.woff
│  │  │      glyphicons-halflings-regular.woff2
│  │  │
│  │  ├─images
│  │  │      code.png
│  │  │
│  │  └─js
│  │          bootstrap-datetimepicker.min.js
│  │          bootstrap.js
│  │          bootstrap.min.js
│  │          jquery-3.5.1.min.js
│  │          npm.js
│  │
│  ├─templates
│  │      admin_add.html
│  │      admin_edit.html
│  │      admin_list.html
│  │      admin_reset.html
│  │      department.html
│  │      depart_add.html
│  │      depart_edit.html
│  │      login.html
│  │      order_list.html
│  │      phonenum_add.html
│  │      phonenum_edit.html
│  │      phonenum_list.html
│  │      template.html
│  │      user_add.html
│  │      user_edit.html
│  │      user_list.html
│  │
│  ├─utils
│  │  │  create_code.py
│  │  │  encrypt.py
│  │  │  form.py
│  │  │  pagenation.py
│  │  │
│  │  └─__pycache__
│  │          create_code.cpython-38.pyc
│  │          encrypt.cpython-38.pyc
│  │          form.cpython-38.pyc
│  │          pagenation.cpython-38.pyc
│  │
│  ├─views
│  │  │  account.py
│  │  │  admins.py
│  │  │  depart.py
│  │  │  order.py
│  │  │  phonenum.py
│  │  │  users.py
│  │  │
│  │  └─__pycache__
│  │          account.cpython-38.pyc
│  │          admins.cpython-38.pyc
│  │          depart.cpython-38.pyc
│  │          order.cpython-38.pyc
│  │          phonenum.cpython-38.pyc
│  │          users.cpython-38.pyc
│  │
│  └─__pycache__
│          admin.cpython-38.pyc
│          apps.cpython-38.pyc
│          models.cpython-38.pyc
│          __init__.cpython-38.pyc
│
├─manageSystem
│  │  asgi.py
│  │  settings.py
│  │  urls.py
│  │  wsgi.py
│  │  __init__.py
│  │
│  └─__pycache__
│          settings.cpython-38.pyc
│          urls.cpython-38.pyc
│          wsgi.cpython-38.pyc
│          __init__.cpython-38.pyc
│
└─__pycache__
        manage.cpython-38.pyc

~~~



###  二、使用方法

1.首先本项目使用的是我本机的mysql数据库，所以刚开始是没有任何数据的，所以要更改配置，连接自己的数据库。

注意：本项目默认电脑已经安装了django,并且掌握python知识，会安装依赖模块。

修改 setting.py的DATABASES配置项如下，在各个配置后填写自己数据库的信息，name:数据库名，host:数据库所在主机的ip地址，如果是本机就填127.0.0.1或localhost, user:数据库用户名，password:密码，port:端口号，mysql数据库默认为3306。

~~~
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':"",
        'HOST':"127.0.0.1",
        'USER':"",
        'PASSWORD':"",
        'PORT':"3306"
    }
}
~~~

2.创建所需的表结构，代码在app/models.py里。打开终端，进入项目，执行如下命令，至此表结构就创建完成。

~~~
python manage.py makemigrations
~~~

~~~
python manage.py migrate
~~~

数据库中所有的表如下：

~~~
+----------------------------+
| Tables_in_managedb         |
+----------------------------+
| app_admin                  |
| app_department             |
| app_phonenumorder          |
| app_prettyphonenum         |
| app_userinfo               |
| auth_group                 |
| auth_group_permissions     |
| auth_permission            |
| auth_user                  |
| auth_user_groups           |
| auth_user_user_permissions |
| django_admin_log           |
| django_content_type        |
| django_migrations          |
| django_session             |
+----------------------------+
15 rows in set (0.01 sec)
~~~

3.在管理员表里添加一条数据，用于登录，sql语句如下：

~~~
insert into app_admin (username,password) values("admin","123456");
~~~

用户名密码可以任意，自己可以更改。

4.启动项目，进入项目，执行如下命令

~~~
python manage.py runserver 8000
~~~

5.访问项目，在浏览器访问本机的8000端口


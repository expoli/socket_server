# 创建项目

django-admin startproject bysms

# 创建项目app

python3 manage.py startapp mgr

# 创建数据库

python3 manage.py migrate

# 定义我们的 数据库表

python3 manage.py startapp common 

# 创建数据库表

## 在项目的配置文件 settings.py 中， INSTALLED_APPS 配置项 加入如下内容


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 加入下面这行
    'common.apps.CommonConfig',
]
‘common.apps.CommonConfig’ 告诉 Django ， CommonConfig 是 common/apps.py 文件中定义的一个应用配置的类。

python3 manage.py makemigrations common

python3 manage.py migrate

# Django Admin 管理数据

python3 manage.py createsuperuser

# 
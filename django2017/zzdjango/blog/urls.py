"""zzdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
#from django.contrib import admin
#from django.urls import path

from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$',views.index),		#第一个参数是正则，所以用^开头，用$结尾，约束为是一个空字符串
    url(r'^hello/$',views.hello),
    #path('hello/',views.hello),
    #path('blog/', bv.hello),	# 要这样写
    #url(r'blog/',bv.hello),	# 这样写也行
]

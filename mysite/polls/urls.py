#/usr/bin/env python
#encoding:utf-8
from django.urls import path
#导入当前模块的视图
from . import views

urlpatterns =[
        path('',views.index,name='index'),
]

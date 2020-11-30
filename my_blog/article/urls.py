# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  : 2020/11/30 21:12
# @Author: Gu Sisong

from django.urls import path
from . import views

# 正在部署的应用的名称
app_name = 'article'

urlpatterns = [
    # path函数将url映射到视图
    path('article-list/', views.article_list, name='article_list'),
]

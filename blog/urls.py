#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by Ben ZHONG on 29/11/18
''
__author__ = "Ben ZHONG"
__date__ = '29/11/18 4:58 PM'

"""

"""

# 
from django.conf.urls import url

from . import views
#

app_name = 'blog' # urls.py 模块是属于 blog 应用的，这种技术叫做视图函数命名空间
urlpatterns = [
    # url(r'^$', views.index, name='index'),
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'index', views.index, name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name='archives'),
    # url(r'^category/(?P<pk>[0-9]+)/$', views.category, name='category'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.CategoryView.as_view(), name='category'),
]



if __name__ == '__main__':
    pass
























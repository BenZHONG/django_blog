#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by Ben ZHONG on 9/12/18
''
__author__ = "Ben ZHONG"
__date__ = '9/12/18 10:06 AM'

"""

"""

# 
from django.conf.urls import url

from . import views
#


app_name = 'comments' # urls.py 模块是属于 comments 应用的，这种技术叫做视图函数命名空间
urlpatterns = [
    url(r'^comment/post/(?P<post_pk>[0-9]+)/$', views.post_comment, name='post_comment'),
]



if __name__ == '__main__':
    pass
























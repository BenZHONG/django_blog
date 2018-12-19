#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by Ben ZHONG on 5/12/18
''
__author__ = "Ben ZHONG"
__date__ = '5/12/18 11:03 AM'

"""

"""

#
from django import template

from ..models import Post, Category
#


register = template.Library()


@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-created_time')[:num]


@register.simple_tag
def archives():
    return Post.objects.dates('created_time', 'month', order='DESC')


@register.simple_tag
def get_categories():
    return Category.objects.all()

if __name__ == '__main__':
    pass
























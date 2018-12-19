#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by Ben ZHONG on 7/12/18
''
__author__ = "Ben ZHONG"
__date__ = '7/12/18 5:17 PM'

"""

"""

# 
from django import forms

from .models import Comment
#


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'url', 'text']



if __name__ == '__main__':
    pass
























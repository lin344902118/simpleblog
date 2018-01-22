# -*- coding:utf-8 -*-
from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    nickname = forms.CharField(max_length=20, widget=forms.TextInput(attrs={"class": 'input', 'placeholder':u'请输入昵称'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": 'input', 'placeholder':u'请输入邮箱'}))
    content = forms.CharField(max_length=500, widget=forms.Textarea(attrs={"class": 'input', 'placeholder':u'请输入评论'}))
    class Meta:
        model = Comment
        fields = ['nickname', 'email', 'content']
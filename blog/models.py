# coding: utf-8
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20, verbose_name=u'类名')
    description = models.CharField(max_length=100, default='', verbose_name=u'描述')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'文章分类'
        verbose_name_plural = verbose_name


class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name=u'标题')
    public_time = models.DateTimeField(auto_now_add=True, verbose_name=u'发布时间')
    author = models.ForeignKey(User, verbose_name=u'作者')
    content = models.TextField(verbose_name=u'内容')
    category = models.ForeignKey(Category, verbose_name=u'分类')
    votes = models.IntegerField(default=0, verbose_name=u'点赞次数')

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'博文'
        verbose_name_plural = verbose_name
        ordering = ['-public_time']


class Comment(models.Model):
    nickname = models.CharField(max_length=20, verbose_name=u'昵称')
    email = models.EmailField(verbose_name=u'邮箱')
    content = models.TextField(max_length=500, verbose_name=u'内容')
    time = models.DateTimeField(auto_now_add=True, verbose_name=u'时间')

    def __unicode__(self):
        return self.nickname

    class Meta:
        verbose_name = u'评论'
        verbose_name_plural = verbose_name
        ordering = ['-time']


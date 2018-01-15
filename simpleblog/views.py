# -*- coding:utf-8 -*-
from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.contrib.auth import logout
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from blog.models import Blog

# Create your views here.
class IndexView(View):
    def get(self, request):
        articles = Blog.objects.all()
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        except EmptyPage:
            page = 1
        p = Paginator(articles, per_page=3, request=request)
        articles = p.page(page)
        return render(request, 'home.html', {'articles': articles})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/index')


class AboutView(View):
    def get(self, request):
        return render(request, 'about.html')
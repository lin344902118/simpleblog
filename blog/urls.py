# -*- coding:utf-8 -*-

from django.conf.urls import url
from views import DetailView, ArticlesView, VotesView

urlpatterns = [
    url(r'^$', ArticlesView.as_view(), name='articles'),
    url(r'^(?P<article_id>\d+)/$', DetailView.as_view(), name='detail'),
    url(r'^votes/$', VotesView.as_view(), name='votes'),
]
from django.shortcuts import render
from django.views.generic.base import View
from blog.models import Blog, Category
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from forms import CommentForm
from django.shortcuts import HttpResponse
import json


# Create your views here.
class ArticlesView(View):
    def get(self, request):
        articles = Blog.objects.all()
        categorys = Category.objects.all()
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        except EmptyPage:
            page = 1
        p = Paginator(articles, per_page=3, request=request)
        articles = p.page(page)
        return render(request, 'articles.html', {'articles': articles, 'categorys': categorys})


class DetailView(View):
    def get(self, request, article_id):
        article = Blog.objects.get(id=int(article_id))
        categorys = Category.objects.all()
        commentForm = CommentForm
        return render(request, 'details.html', {'article': article, 'categorys': categorys, 'commentForm': commentForm})


class VotesView(View):
    def post(self, request):
        result = dict()
        try:
            article_id = request.POST.get('article_id', '')
            if not article_id:
                e = 'id error'
                raise Exception, e
            article = Blog.objects.get(id=article_id)
            article.votes += 1
            article.save()
            result['ret'] = 0
            result['status'] = 'success'
        except Exception, e:
            result['ret'] = 10000
            result['status'] = 'failed'
            result['message'] = str(e)
        return HttpResponse(json.dumps(result), content_type="application/json")

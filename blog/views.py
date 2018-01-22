from django.shortcuts import render, HttpResponse, redirect
from django.views.generic.base import View
from blog.models import Blog, Category, Comment
from simpleblog.views import pagn
from .forms import CommentForm
import json


# Create your views here.
class ArticlesView(View):
    def get(self, request):
        articles = Blog.objects.all()
        categorys = Category.objects.all()
        articles = pagn(request, articles)
        return render(request, 'articles.html', {'articles': articles, 'categorys': categorys})


class DetailView(View):
    def get(self, request, article_id):
        article = Blog.objects.get(id=int(article_id))
        categorys = Category.objects.all()
        comments = Comment.objects.filter(article=article)
        commentForm = CommentForm
        # article.content = article.content.replace('\n', '</p><p>')
        return render(request, 'details.html',
                      {'article': article, 'categorys': categorys, 'comments': comments,'commentForm': commentForm})


class VotesView(View):
    def post(self, request):
        result = dict()
        try:
            article_id = request.POST.get('article_id', '')
            if not article_id:
                e = 'id error'
                raise e
            article = Blog.objects.get(id=article_id)
            article.votes += 1
            article.save()
            result['ret'] = 0
            result['status'] = 'success'
        except Exception as e:
            result['ret'] = 10000
            result['status'] = 'failed'
            result['message'] = str(e)
        return HttpResponse(json.dumps(result), content_type="application/json")


class CommentView(View):
    def post(self, request):
        form = CommentForm(request.POST)
        article_id = request.POST.get('id', '')
        if not article_id:
            e = 'id error'
            raise e
        if form.is_valid():
            cd = form.cleaned_data
            article = Blog.objects.get(id=article_id)
            comment = Comment.objects.create(nickname=cd['nickname'],
                                             email=cd['email'],
                                             content=cd['content'],
                                             article = article)
            if comment:
                return redirect('/article/%s' %article_id)
        categorys = Category.objects.all()
        commentForm = CommentForm()
        return render(request, 'details.html', {'article': article, 'categorys': categorys, 'commentForm': commentForm})


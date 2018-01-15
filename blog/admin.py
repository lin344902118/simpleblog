# encoding: utf-8
from django.contrib import admin
from .models import Blog, Category

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    class Media:
        js = (
            '/static/js/editor/kindeditor/kindeditor-all.js',
            '/static/js/editor/kindeditor/lang/zh-CN.js',
            '/static/js/editor/kindeditor/config.js',
        )


class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Blog, BlogAdmin)
admin.site.register(Category)
# encoding: utf-8
from django.contrib import admin
from .models import Blog, Category

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "category", "public_time", "votes")
    search_fields = ("title", "author", "category")
    list_filter = ("public_time", "votes")
    ordering = ("-public_time",)

    class Media:
        js = (
            '/static/js/jquery-3.2.1.min.js',
            '/static/js/tinymce/js/tinymce/tinymce.min.js',
            '/static/js/tinymce/js/tinymce/jquery.tinymce.min.js',
            '/static/js/tinymce/js/tinymce/textareas.js'
        )


class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Blog, BlogAdmin)
admin.site.register(Category)
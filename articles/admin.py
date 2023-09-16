from django.contrib import admin
from .models import *

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "desc", "date",)
    search_fields = ("name__startswith",)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("post", "author", "body")
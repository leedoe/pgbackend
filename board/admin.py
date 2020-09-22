from django.contrib import admin

from .models import Category, Comment, Post


@admin.register(Post)
class PostAdmim(admin.ModelAdmin):
    list_display = ['pk', 'title', 'writer', 'writer_name']
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

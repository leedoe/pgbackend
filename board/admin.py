from django.contrib import admin

from .models import Category, Comment, Post


@admin.register(Post)
class PostAdmim(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

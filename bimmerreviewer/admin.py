""" Import the post model that was created in the models.py file
    and register it in the admin area.
"""
from django.contrib import admin
from .models import Post, Comments, Category

admin.site.register(Category)


@admin.register(Comments)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'body', 'approve')
    list_filter = ('author', 'date_comment')
    actions = ['approve_comment']

    def approve_comment(self, request, queryset):
        queryset.update(approve=True)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'body', 'price', 'approved')
    list_filter = ('author', 'create_date')
    actions = ['approved_posts']

    def approved_posts(self, request, queryset):
        queryset.update(approved=True)

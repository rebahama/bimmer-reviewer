""" Import the post model that was created in the models.py file
    and register it in the admin area.
"""
from django.contrib import admin
from .models import Post, Comments


admin.site.register(Comments)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'body', 'price', 'approved')
    list_filter = ('author', 'create_date')
    actions = ['approved_posts']
    
    
    def approved_posts(self, request, queryset):
        queryset.update(approved=True)
 
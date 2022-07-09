""" Import the post model that was created in the models.py file
    and register it in the admin area.
"""
from django.contrib import admin
from .models import Post, Comments

admin.site.register(Post)
admin.site.register(Comments)

""" Registering the name of the project to Django"""
from django.apps import AppConfig


class BimmerreviewerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bimmerreviewer'

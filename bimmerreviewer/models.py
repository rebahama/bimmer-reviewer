"""Importing the django models and clouinary for image use
"""
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.urls import reverse


class Post(models.Model):
    """ Create a model database for creating a post
"""
    title = models.CharField(max_length=250, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = CloudinaryField('image', default='placeholder')
    body = models.TextField(max_length=1500)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title + '  ' + str(self.author)

    def get_absolute_url(self):
        """ Return to the html file below after POST the data"""
        return reverse('home')

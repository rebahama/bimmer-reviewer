"""Importing the django models and clouinary for image use
"""
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200)


class Post(models.Model):
    """ Create a model database for creating a post
        adding a tuple so that the user can pre choose
        in a dropdown window what year they want to post.
"""
    ENGINE_YEAR = (
        ('2000', '2000'),
        ('2001', '2001'),
        ('2002', '2002'),
        ('2003', '2003'),
        ('2004', '2004'),
        ('2005', '2005'),
        ('2006', '2006'),
        ('2007', '2007'),
        ('2008', '2008'),
        ('2009', '2009'),
        ('2010', '2010'),
        ('2011', '2011'),
        ('2012', '2012'),
        ('2013', '2013'),
        ('2014', '2014'),
        ('2015', '2015'),
        ('2016', '2016'),
        ('2017', '2017'),
        ('2018', '2018'),
        ('2019', '2019'),
        ('2020', '2020'),
        ('2021', '2021'),
        ('2022', '2022'),
    )

    FUEL_TYPE = (
        ('Diesel', 'Diesel'),
        ('Petrol', 'Petrol'),
        ('Other',  'Other'),
        )

    CATEGORY_CAR = (
        ('1-SERIES', '1-SERIES'),
        ('3-SERIES', '3-SERIES'),
        ('5-SERIES', '5-SERIES'),
        ('OTHER', 'OTHER'),
    )

    title = models.CharField(max_length=250, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    year = models.CharField(max_length=10, choices=ENGINE_YEAR, default='Year')
    price = models.IntegerField(blank=True, default=0)
    fuel_type = models.CharField(max_length=10, choices=FUEL_TYPE, default='OTHER')
    image = CloudinaryField('image', default='placeholder', null=False)
    category = models.CharField(max_length=200, choices=CATEGORY_CAR, default='OTHER')
    body = models.TextField(max_length=1500)
    create_date = models.DateTimeField(auto_now_add=True)
    like = models.ManyToManyField(User, related_name='review_like', blank=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.title + '  ' + str(self.author)

    def all_likes(self):
        return self.like.count()

    def get_absolute_url(self):
        """ Return to the html file below after POST the data"""
        return reverse('home')


class Comments(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    author = models.CharField(max_length=255)
    body = models.TextField()
    date_comment = models.DateTimeField(auto_now_add=True)
    approve = models.BooleanField(default=False)

    def __str__(self):
        return str(self.post)

    def get_absolute_url(self):
        """ Return to the html file below after POST the data"""
        return reverse('home')

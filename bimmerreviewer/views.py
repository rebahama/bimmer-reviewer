from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from . models import Post


class Firstview(ListView):
    model = Post
    template_name = 'home.html'


class DetailReview(DetailView):
    model = Post
    template_name = 'detail-review.html'


class CreateReview(CreateView):
    model = Post
    template_name = 'create-review.html'
    fields = '__all__'

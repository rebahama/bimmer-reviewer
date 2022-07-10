from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from . models import Post, Comments


def homepage(request):
    """Render the html file below"""
    return render(request, 'index.html')


class Firstview(ListView):
    """Show all the data from the queryset """
    model = Post
    template_name = 'home.html'


class DetailReview(DetailView):
    """ Only showing the detalied view when clicked
    on the "Firstview"""
    model = Post
    template_name = 'detail-review.html'


class CreateReview(CreateView):
    """ Create a new view and render it in the template below"""
    model = Post
    template_name = 'create-review.html'
    fields = '__all__'


class UpdateReview(UpdateView):
    """ Update the view and the fileds that are below
    """
    model = Post
    template_name = 'update-review.html'
    fields = ['title', 'year', 'body', 'image']


class DeleteReview(DeleteView):
    """Delete the view that is shown"""
    model = Post
    template_name = 'delete-review.html'
    fields = ['title', 'body', 'image']
    success_url = reverse_lazy('home')


class AddComment(CreateView):
    """Adding comments to a review"""
    model = Comments
    template_name = 'add-comments.html'
    fields = ['author', 'post', 'body']

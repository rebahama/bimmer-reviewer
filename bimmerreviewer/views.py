""" Importing all the methods to use for the view
    this file is responsible for querying data and
    displaying,delete,edit show the model that is created
    in the model file
"""
from django.contrib.messages.views import SuccessMessageMixin, messages
from django.shortcuts import render, get_object_or_404
from django.views.generic import (ListView, DetailView, CreateView,
                                  UpdateView, DeleteView)
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from . models import Post, Comments


def error_404(request, exepction):
    """ handles error of "page of not found"""

    return render(request, '404.html')


def error_500(request, *args, **kwargs):
    """ handles error of "page of not found"""

    return render(request, '500.html')


def contact_us(request):
    """ render the contact us html"""
    return render(request, 'contact-us.html')


def category_review(request, series):
    """Method for rendering the html file below
        and for grasping the category variable in the
        model that is named Post. After grasping the category variable
         put it in a context dictionary so that we can use it as a template tag
         in the html file"""
    category_specefic = Post.objects.filter(category=series).order_by("-create_date")
    return render(request, 'categories.html',
                           {'series': series,
                            'category_specefic': category_specefic})


def home_page(request):
    """Render the html file below"""
    return render(request, 'index.html')


def like_review(request, pk):
    """Retrive the id of post that is renderd and then"
        add a like to that current user with the refrence
        of the post.id number
    """
    post = get_object_or_404(Post, id=request.POST.get('post_like_id'))
    if post.like.filter(id=request.user.id).exists():
        post.like.remove(request.user)
        messages.success(request, "You have unliked this post")

    else:
        post.like.add(request.user)
        messages.success(request, "You have liked this post")
    return HttpResponseRedirect(reverse('detail-review', args=[str(pk)]))


def search_list(request):
    """ requst the html input that is named 'searched result' and
        put it in a variable, after query only the result that contains
        the title variable from the models.py file.
    """
    if request.method == "POST":
        searching = request.POST.get('search-result')
        search_post = Post.objects.filter(title__contains=searching)
        return render(request, 'search-result.html',
                      {'searching': searching, 'search_post': search_post})
    else:
        return render(request, 'search-result.html',
                      {'searching': searching, 'search_post': search_post})


class FirstView(ListView):
    """Show all the data from the queryset only if admin approves
       it and order it by the date
    """
    queryset = Post.objects.filter(approved=True)
    ordering = ['-create_date']
    template_name = 'home.html'


class UserView(ListView):
    """ Render the view below on the user review html file
        this queryset shows the posts that have been created
        by the user.
    """
    queryset = Post.objects.filter(approved=True)
    ordering = ['-create_date']
    template_name = 'user-reviews.html'


class DetailReview(DetailView):
    """ Only showing the detalied view when clicked
    on the "Firstview"""
    model = Post
    template_name = 'detail-review.html'


class CreateReview(SuccessMessageMixin, CreateView):
    """ Create a new view and render it in the template below, request
    the user author from the method and use that user as the autor so that
    only that specific user can post the review"""
    model = Post
    template_name = 'create-review.html'
    fields = ['title', 'price', 'year', 'fuel_type', 'body',
              'category', 'image']
    success_message = 'Review successfully created awaiting admin approval'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdateReview(SuccessMessageMixin, UpdateView):
    """ Update the view and the fileds that are below
    After the update view have been sent via the form
    return to the same page with the help of primary key
    in the url.
    """
    model = Post
    template_name = 'update-review.html'
    fields = ['title', 'price', 'year', 'fuel_type', 'body',
              'category', 'image']

    def get_success_url(self):
        update_id = self.kwargs['pk']
        return reverse_lazy('detail-review', kwargs={'pk': update_id})

    success_message = "Review have been successfully updated"


class DeleteReview(SuccessMessageMixin, DeleteView):
    """Delete the view that is shown"""
    model = Post
    template_name = 'delete-review.html'
    fields = ['title', 'body', 'image']
    success_url = reverse_lazy('home')

    def get_success_url(self):
        messages.success(self.request, "Review have been successfully deleted")
        return reverse('home')


class AddComment(SuccessMessageMixin, CreateView):
    """Adding comments to a review the function that check
    if form is valid takes the primary key of the post_id
    to determine what post is in the url and then
    add the comment to that specific post id"""
    model = Comments
    template_name = 'add-comments.html'
    fields = ['author', 'body']
    success_message = "Comment have been successfully added"

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

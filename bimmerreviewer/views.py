from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from . models import Post, Comments


def homepage(request):
    """Render the html file below"""
    return render(request, 'index.html')


def LikeReview(request, pk):
    """Retrive the id of post that is renderd and then"
        add a like to that current user with the refrence
        of the post.id number
    """
    post = get_object_or_404(Post, id=request.POST.get('post_like_id'))
    post.like.add(request.user)
    return HttpResponseRedirect(reverse('detail-review', args=[str(pk)]))


class Firstview(ListView):
    """Show all the data from the queryset only if admin approves it """
    queryset = Post.objects.filter(approved=True)
    template_name = 'home.html'


class DetailReview(DetailView):
    """ Only showing the detalied view when clicked
    on the "Firstview"""
    model = Post
    template_name = 'detail-review.html'


class CreateReview(CreateView):
    """ Create a new view and render it in the template below, request
    the user author from the method and use that user as the autor so that
    onyl that specifik user can post the review"""
    model = Post
    template_name = 'create-review.html'
    fields = ['title', 'price', 'year', 'body', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


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
    """Adding comments to a review the function that check
    if form is valid takes the primary key of the post_id
    to determine what post is in the url and then
    add the comment to that specific post id"""
    model = Comments
    template_name = 'add-comments.html'
    fields = ['author', 'body']

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)


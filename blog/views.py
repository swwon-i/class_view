from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Post

# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name  = 'posts'

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

class PostCreateView(CreateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['title', 'content']
    success_url = '/blog'

class PostUpdateView(UpdateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['title', 'content']
    success_url = '/blog'

class PostDeleteView(DeleteView):
    model = Post
    # template_name = 'blog/post_confirm_delete.html'
    success_url = '/blog'
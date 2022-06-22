from django.urls import reverse_lazy
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.views import generic
from django.views.generic.edit import DeleteView
from .models import Post


# Create your views here.

class PostListView(generic.ListView):
    model = Post
    context_object_name = 'post_lists'

class PostCreateView(generic.CreateView):
    model = Post
    fields = "__all__"
    success_url  = reverse_lazy("blog:all")

class PostDetailView(generic.DetailView):
    model = Post

class PostUpdateView(generic.UpdateView):
    model = Post
    fields = "__all__"
    success_url  = reverse_lazy("blog:all")

class PostDeleteView(DeleteView):
    model = Post
    fields = "__all__"
    success_url  = reverse_lazy("blog:all")
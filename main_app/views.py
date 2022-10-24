from django.shortcuts import render

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post
# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def posts_index(request):
    posts = Post.objects.all()
    return render(request, 'posts/index.html', { 'posts': posts})

def posts_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'posts/detail.html', { 'post': post })


class PostCreate(CreateView):
  model = Post
  fields = '__all__'
  success_url = '/posts/'
  
class PostUpdate(UpdateView):
    model = Post
    fields = ['year', 'model']

class PostDelete(DeleteView):
    model = Post
    success_url = '/posts/'
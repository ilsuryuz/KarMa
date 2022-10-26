from audioop import reverse
from wsgiref.util import request_uri
from django.shortcuts import get_object_or_404, redirect, render

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from .models import Post, Profile
from .forms import ProfileForm
# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def posts_index(request):
    posts = Post.objects.all()
    return render(request, 'posts/index.html', { 'posts': posts})

@login_required
def posts_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'posts/detail.html', { 'post': post })

class PostCreate(LoginRequiredMixin, CreateView):
  model = Post
  fields = ['year', 'mark', 'model', 'content', 'photo']
  
  def form_valid(self, form):
      form.instance.user = self.request.user
      
      return super().form_valid(form)
  
class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['year', 'mark', 'model', 'content', 'photo']

class PostDelete(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = '/posts/'

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(
                user=user
            )
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message }
    return render(request, 'registration/signup.html', context)
@login_required
def profile(request):
    profile = request.user.profile
    profile_form = ProfileForm(instance=profile)
    
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        if profile_form.is_valid():
            profile_form.save()
    return render(request, 'profile/profile.html', { 'profile_form': profile_form, 'profile': profile})
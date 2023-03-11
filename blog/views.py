from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

# Create your views here.
class BlogLisView(ListView):
    model = Post
    template_name = 'main.html'
    


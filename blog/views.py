from django.shortcuts import render
from django.views.generic import ListView

from blog.models import Post


# Create your views here.

class PostList(ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'post_list.html'
    context_name = 'post_list'
    paginate_by = 6

from django.shortcuts import render
from .models import Post


# Create your views here.


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})


def post_details(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'post_details.html', {'post': post})

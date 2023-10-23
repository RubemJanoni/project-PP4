from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from django.urls import reverse_lazy
from blog.models import Post
from django.views.generic import TemplateView
from .form import *


class Initial_page(TemplateView):
    template_name = 'blog.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['publica'] = Post.objects.all()

        return context


class CreatePost(CreateView):
    model = Post
    # fields = '__all__'
    form_class = Publication_form
    excludes = ['likes']
    template_name = 'pages/painel.html'
    success_url = reverse_lazy('blog:List_publication')

    # Método que envia informações complementares para o template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_page'] = "Create your post"
        context['description_page'] = "Use the form below to create a post"
        context['button_name'] = "Submit"

        return context


class ListaPost(ListView):
    model = Post
    template_name = 'pages/lista.html'
    # Método que envia informações complementares para o template

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_page'] = "All Posts"
        context['description_page'] = "All Blog Posts"
        context['main'] = "Post"
        return context


class UpdatePost(UpdateView):
    model = Post
    form_class = Publication_form
    template_name = 'pages/painel.html'
    success_url = reverse_lazy('blog:List_publication')

    # Método que envia informações complementares para o template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_page'] = "Update User"
        context['description_page'] = "Use the form below to update the post"
        context['button_name'] = "Update Post"
        return context


class DeletePost(DeleteView):
    model = Post
    template_name = 'pages/painel.html'
    success_url = reverse_lazy('blog:List_publication')

    # Método que envia informações complementares para o template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_page'] = "Delete User"
        context['description_page'] = "Use the form below to delete the post"
        context['button_name'] = "Delete Post"
        return context

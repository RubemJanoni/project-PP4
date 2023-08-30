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
    template_name = 'blog/pages/painel.html'
    success_url = reverse_lazy('Access_Control:List_publication')

    # Método que envia informações complementares para o template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_page'] = "Crie sua postagem"
        context['description_page'] = "Use o formulário abaixo para criar novas postagens"
        context['button_name'] = "Publicar Postagem"

        return context


class ListaPost(ListView):
    model = Post
    template_name = 'blog/pages/lista.html'
    success_url = reverse_lazy('Access_Control:Make_login')

    # Método que envia informações complementares para o template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_page'] = "Todas as postagens"
        context['description_page'] = "Relação de todos as postagens no sistema"
        context['main'] = "Postagem"
        return context


class UpdatePost(UpdateView):
    model = Post
    form_class = Publication_form
    template_name = 'blog/pages/painel.html'
    success_url = reverse_lazy('Access_Control:List_user')

    # Método que envia informações complementares para o template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_page'] = "Atualiza usuario"
        context['description_page'] = "Use o formulário abaixo para atualizar a postagem"
        context['button_name'] = "Atualizar postagem"
        return context


class DeletePost(DeleteView):
    model = Post
    template_name = 'blog/pages/painel.html'
    success_url = reverse_lazy('Access_Control:List_user')

    # Método que envia informações complementares para o template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_page'] = "Exclui usuario"
        context['description_page'] = "Use o formulário abaixo para excluir um usuário"
        context['button_name'] = "Deletar publicação"
        return context

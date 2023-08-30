from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.models import User


# Create your views here.
class Make_login (LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('blog:List_publication')


class Logout (LoginRequiredMixin, LogoutView):
    success_url = reverse_lazy('Access_Control:Make_login')


class CreateUser(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'pages/painel.html'
    success_url = reverse_lazy('Access_Control:Make_login')

    # Método que envia informações complementares para o template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_page'] = "Registro de Usuários"
        context['description_page'] = "Use o formulário abaixo para criar novos usuários"
        context['button_name'] = "Criar novo usuario"
        context['object_list'] = User.objects.all()

        return context


class UpdateUser(UpdateView):
    model = User
    form_class = UserCreationForm
    template_name = 'pages/painel.html'
    success_url = reverse_lazy('Access_Control:List_user')

    # Método que envia informações complementares para o template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_page'] = "Atualiza usuario"
        context['description_page'] = "Use o formulário abaixo para atualizar as informações de login do usuário"
        context['button_name'] = "Criar novo usuario"
        context['object_list'] = User.objects.all()
        return context


class DeleteUser(DeleteView):
    model = User
    template_name = 'pages/painel.html'
    success_url = reverse_lazy('Access_Control:List_user')

    # Método que envia informações complementares para o template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_page'] = "Exclui usuario"
        context['description_page'] = "Use o formulário abaixo para excluir um usuário"
        context['button_name'] = "Deletar usuario"
        return context


class ListaUser(ListView):
    model = User
    template_name = 'pages/lista.html'
    success_url = reverse_lazy('Access_Control:Make_login')

    # Método que envia informações complementares para o template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_page'] = "Todos os usuarios"
        context['description_page'] = "Relação de todos os usuarios cadastrados no sistema"
        return context

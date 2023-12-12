from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib import messages
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.models import User


# Create your views here.
class Make_login (LoginView):
    template_name = 'login.html'    

    def get_success_url(self):
        return reverse_lazy('blog:List_publication')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Login successfully. Welcome!')
        return response

    def form_invalid(self, form):
        response = super().form_invalid(form)
        messages.error(self.request, 'Something is wrong, Try again.')
        return response

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            # Redirecionar usuário autenticado para a página desejada
            return redirect(self.get_success_url())
        return super().get(request, *args, **kwargs)


class CustomLogoutView (LoginRequiredMixin, LogoutView):
    template_name = 'logout.html' 

    def get(self, request, *args, **kwargs):
        messages.success(request, 'Logout successfully')

        return render(request, self.template_name)


class SimpleUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Personalize os rótulos dos campos, se necessário
        self.fields['username'].label = 'Username'
        self.fields['email'].label = 'Email'
        self.fields['password1'].label = 'Password'
        self.fields['password2'].label = 'Password confirmation'

        self.fields['username'].help_text = None
        self.fields['password2'].help_text = None
        self.fields['password1'].help_text = None
        

    def clean_username(self):
        username = self.cleaned_data['username']
        # Adicione validações adicionais se necessário
        return username


class CreateUser(CreateView):
    model = User
    form_class = SimpleUserCreationForm
    template_name = 'painel.html'
    success_url = reverse_lazy('access_control:Make_login')

    # Método que envia informações complementares para o template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_page'] = "Register"
        context['description_page'] = "Create an account"
        context['button_name'] = "Create"
        context['object_list'] = User.objects.all()

        return context


class UpdateUser(UpdateView):
    model = User
    form_class = UserCreationForm
    template_name = 'painel.html'
    success_url = reverse_lazy('access_control:List_user')

    # Método que envia informações complementares para o template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_page'] = "Update User"
        context['description_page'] = "Use the form below to update new users"
        context['button_name'] = "Create new user"
        context['object_list'] = User.objects.all()
        return context


class DeleteUser(DeleteView):
    model = User
    template_name = 'painel.html'
    success_url = reverse_lazy('access_control:List_user')

    # Método que envia informações complementares para o template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_page'] = "Delete User"
        context['description_page'] = "Use the form below to delete new users"
        context['button_name'] = "Delete new user"
        return context


class ListaUser(ListView):
    model = User
    template_name = 'lista.html'
    success_url = reverse_lazy('access_control:Make_login')

    # Método que envia informações complementares para o template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_page'] = "Users"
        context['description_page'] = "All users registered"
        return context

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate

# Create your views here.
# home project


def home(request):
    return render(request, 'index.html')


def signup(request):

    if request.method == 'GET':
        return render(request, 'signup.html', {

            'form': UserCreationForm,

        })

    else:
        if request.POST['password1'] == request.POST['password2']:

            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()

                login(request, user)
                return redirect('tasks')

            except:

                return render(request, 'signup.html', {

                    'form': UserCreationForm,
                    "error": 'User already exist'

                })

        return render(request, 'signup.html', {

            'form': UserCreationForm,
            "error": 'Password different'

        })

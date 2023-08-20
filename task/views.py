from django.shortcuts import render

# Create your views here.
# home project


def home(request):
    return render(request, 'index.html')


def signup(request):
    return render(request, 'signup.html')

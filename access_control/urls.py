from django.contrib import admin
from django.urls import path, include
from access_control.views import *
from blog.views import *

app_name = 'access_control'

urlpatterns = [
    path('login/', Make_login.as_view(), name='Make_login'),
    path('logout/', CustomLogoutView.as_view(), name='Make_logout'),
    path('users/', ListaUser.as_view(), name='List_user'),
    path('create/', CreateUser.as_view(), name='Create_user'),
    path('update/<int:pk>', UpdateUser.as_view(), name='Update_user'),
    path('delete/<int:pk>', DeleteUser.as_view(), name='Delete_user'),
]

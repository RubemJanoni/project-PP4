from django.contrib import admin
from django.urls import path, include
from Access_Control.views import *
from Blog.views import *

app_name = 'Access_Control'

urlpatterns = [
    path('', Make_login.as_view(), name='Make_login'),
    path('logout/', Logout.as_view(), name='Make_logout'),
    path('users/', ListaUser.as_view(), name='List_user'),
    path('create/', CreateUser.as_view(), name='Create_user'),
    path('update/<int:pk>', UpdateUser.as_view(), name='Update_user'),

    path('delete/<int:pk>', DeleteUser.as_view(), name='Delete_user'),
]

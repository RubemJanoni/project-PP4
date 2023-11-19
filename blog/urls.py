from django.contrib import admin
from django.urls import path, include
from access_control.views import *
from blog.views import *

app_name = 'blog'

urlpatterns = [
    path('', Initial_page.as_view(), name='Home'),
    path('publication/criar/', CreatePost.as_view(),
     name='Create_publication'),
    path('publication/listar/', ListaPost.as_view(), name='List_publication'),
    path('publication/update/<int:pk>',
         UpdatePost.as_view(), name='Update_publication'),
    path('publication/delete/<int:pk>',
         DeletePost.as_view(), name='Delete_publication'),
]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Access_Control.urls')),
   # path('', include('Blog.urls')),
]

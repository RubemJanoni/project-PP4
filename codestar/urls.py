from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('access_control.urls')),
    path('', include('blog.urls')),
]

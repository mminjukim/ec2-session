from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin777mj/', admin.site.urls),
    path('', include('posts.urls')),
]

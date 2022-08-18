"""django_puppy_store URL Configuration.
"""
from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^', include('puppies.urls')),
    re_path(
        r'^api-auth',
        include('rest_framework.urls', namespace='rest_framework')
    )
]

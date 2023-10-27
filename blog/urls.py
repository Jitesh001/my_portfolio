# notes/urls.py
from django.urls import path
from . import views

app_name = 'blogs'

urlpatterns = [
    path('', views.blog_page, name='blog-page'),
]

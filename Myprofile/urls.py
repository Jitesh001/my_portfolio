# Myprofile/urls.py

from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('resume-download/<str:title>/', views.ResumeDownloadView.as_view(), name='resume-download'),
    path('contact/', views.contact_us, name='contact_us'),
]
# notes/urls.py
from django.urls import path
from . import views

app_name = 'notes'

urlpatterns = [
    path('', views.NoteListView.as_view(), name='note-list'),
    path('note-download/<int:pk>/', views.NoteDownloadView.as_view(), name='note-download'),
    path('view-pdf/<int:note_id>/', views.display_pdf, name='display-pdf'),
    # Add more URL patterns for detail and download views if needed
]

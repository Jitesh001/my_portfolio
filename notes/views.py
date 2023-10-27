from django.views.generic import ListView
from django.views import View
from django.http import FileResponse, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Note
from django.conf import settings
from django.http import Http404
import mimetypes
import os

class NoteListView(ListView):
    model = Note
    template_name = 'notes/note_list.html'
    context_object_name = 'notes'

class NoteDownloadView(View):
    def get(self, request, pk):
        try:
            note = get_object_or_404(Note, pk=pk)
            response = HttpResponse(note.pdf_file, content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="{note.title}.pdf"'
            return response
        except Http404:
            return HttpResponse("Notes not found", status=404)
    

def display_pdf(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    return render(request, 'notes/display_pdf.html', {'note': note})

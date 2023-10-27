# Myprofile/views.py

from django.shortcuts import render, get_object_or_404
from django.http import FileResponse, HttpResponse
from django.conf import settings
import os
from .models import ContactMessage, Resume
from .forms import ContactForm
from django.views import View
from django.http import Http404
from django.core.exceptions import ValidationError

def home(request):
    return render(request, 'Myprofile/profile.html')

class ResumeDownloadView(View):
    def get(self, request, title):
       try:
            resume = get_object_or_404(Resume, resumetitle=str(title))
            response = HttpResponse(resume.pdf_file, content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="Jitesh_shewale_resume.pdf"'
            return response
       except Http404:
            return render(request, 'Myprofile/noresume.html')
       
def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        try:
            if form.is_valid():
                name = form.cleaned_data['name']
                email = form.cleaned_data['email']
                subject = form.cleaned_data['subject']
                message = form.cleaned_data['message']

                # Save the message to the database
                ContactMessage.objects.create(
                    name=name,
                    email=email,
                    subject=subject,
                    message=message
                )
                # Redirect or display a thank you page
                return render(request, 'Myprofile/thanku.html')
        except ValidationError as e:
            return HttpResponse('Error with page', status=404)
            form.add_error(None, e)
    else:
        form = ContactForm()

    return render(request, 'Myprofile/contact.html', {'form': form})


def custom_404(request, exception):
    return render(request, '404.html', status=404)

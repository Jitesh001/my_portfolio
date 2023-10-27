# notes/models.py
from django.db import models
from django.utils import timezone
import pytz

class Note(models.Model):
    title = models.CharField(max_length=200)
    pdf_file = models.FileField(upload_to='notes/')
    ist = pytz.timezone('Asia/Kolkata')  # Create a time zone object for IST.
    timestamp = models.DateTimeField(default=timezone.now().astimezone(ist))

    def __str__(self):
        return self.title

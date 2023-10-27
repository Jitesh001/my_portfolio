from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    def __str__(self):
        return self.name

class Resume(models.Model):
    resumetitle = models.CharField(max_length=100)
    pdf_file = models.FileField(upload_to='resumes/')
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.resumetitle
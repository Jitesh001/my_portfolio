from django.shortcuts import render
from django.views import View

# Create your views here.
def blog_page(request):
    return render(request, 'blog/index.html')
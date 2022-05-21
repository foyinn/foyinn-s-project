# Create your views here.
from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    return render(request, "homes/index.html")

def about(request):
    return render(request, 'homes/about.html')

def contact(request):
    return render(request, 'homes/contact.html')


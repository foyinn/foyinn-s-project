# Create your views here.

from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1> Welcome!</h1>')

def about(request):
    return HttpResponse('<h1> About us.</h1>')

def contact(request):
    return HttpResponse('<h1> Get in touch.</h1>')


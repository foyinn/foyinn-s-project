from django.urls import path
from .views import home, about, contact

urlpatterns = [
   path('', home),
   path('about-me/', about),
   path('contact-me/', contact)
]
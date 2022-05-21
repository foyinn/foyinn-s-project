from django.urls import path
from .views import home, about, contact

urlpatterns = [
   path('', home),
   path('aboutme/', about),
   path('contactme/', contact)
]
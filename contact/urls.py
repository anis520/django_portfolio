from django.contrib import admin
from .views import contact
from django.urls import path

urlpatterns = [
    path('contact/', contact),
 
]

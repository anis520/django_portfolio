from django.contrib import admin
from django.urls import path
from .views import me 
urlpatterns = [
    path('', me),
]

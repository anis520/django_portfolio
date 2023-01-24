from django.contrib import admin
from django.urls import path,include
from .views import skill

urlpatterns = [
    path('skills/', skill),
 
]

from django.shortcuts import render
from .models import Project_name
# Create your views here.
def projects(req):
    datas =Project_name.objects.all()
    return render(req,'projects/projects.html',{'stu':datas})
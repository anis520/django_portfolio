from django.shortcuts import render

# Create your views here.
def projects(req):
    return render(req,'projects/projects.html')
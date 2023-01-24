from django.shortcuts import render

# Create your views here.
def service(req):
    return render(req,'service/service.html')
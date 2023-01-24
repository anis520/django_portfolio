from django.shortcuts import render

# Create your views here.
def me(req):
    return render(req,'me/me.html')
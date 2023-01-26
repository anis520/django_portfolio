from django.shortcuts import render
from .forms import FormData
from .models import Textname

# Create your views here.
def contact(req):
    if req.method=='POST':
     print('its post method')   
     fm=FormData(req.POST)
     name=req.POST['name']
     email=req.POST['email']
     text=req.POST['text']
     if fm.is_valid():
      print(fm.cleaned_data,name)
    #  Textname.objects.create(Name=name,Text=text,Email=email)
     Text=Textname(Name=name,Email=email,Text=text)
     Text.save()
     fm=FormData()

     return render(req,'contact/contact.html',{'fm':fm,'name':name,'msg':' Your data is succrss fully  sended'}) 
    else:
     fm=FormData()
    return render(req,'contact/contact.html',{'fm':fm})
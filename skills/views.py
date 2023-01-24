from django.shortcuts import render
from  skills.models import Skill_name
from .forms import Data_form



# Create your views here.d
def skill(req):
    fm=Data_form()
    skills =Skill_name.objects.all()
    return render(req,'skills/skills.html',{'stu':skills})
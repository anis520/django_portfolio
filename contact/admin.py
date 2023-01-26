from django.contrib import admin

# Register your models here.
from .models import Textname


@admin.register(Textname)


class TextnameAdmin(admin.ModelAdmin):
    list_display=('Name','Email','Text')

# admin.site.register(Skill_name,Skill_nameAdmin)
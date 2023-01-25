from django.contrib import admin

# Register your models here.
from .models import Project_name


@admin.register(Project_name)


class Project_nameAdmin(admin.ModelAdmin):
    list_display=('projectName','projectLink','projectText','projectPhoto')

# admin.site.register(Skill_name,Skill_nameAdmin)
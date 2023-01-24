from django.contrib import admin

# Register your models here.
from .models import Skill_name


@admin.register(Skill_name)


class Skill_nameAdmin(admin.ModelAdmin):
    list_display=('id', 'skillName','skillLength')

# admin.site.register(Skill_name,Skill_nameAdmin)
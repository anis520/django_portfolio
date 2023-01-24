from django.db import models

# Create your models here.
class Skill_name(models.Model):
    skillName=models.CharField(max_length=50)
    skillLength=models.IntegerField()
    def __str__(self):
        return self.skillName
from django.db import models

# Create your models here.
class Project_name(models.Model):
    projectName=models.CharField(max_length=50)
    projectPhoto=models.CharField(max_length=2000)
    projectLink=models.CharField(max_length=1000)
    projectText=models.CharField(max_length=1000)
    def __str__(self):
        return self.projectName
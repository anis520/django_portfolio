from django.db import models

# Create your models here.
class Textname(models.Model):
    Name=models.CharField(max_length=20)
    Email=models.EmailField()
    Text=models.CharField(max_length=1000)
     
    def __str__(self):
        return self.Name
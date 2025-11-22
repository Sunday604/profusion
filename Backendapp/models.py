from django.db import models

# Create your models here.

class Datebase(models.Model):
    name=models.CharField(max_length=50)
    phone=models.CharField(max_length=20,blank=True)
    email=models.EmailField(blank=True)
    message=models.TextField(blank=True, null=True)


    def __str__(self):
        return self.name
    


from django.db import models

# Create your models here.
class Blog(models.Model):
    email=models.EmailField(max_length=100,blank=True)
    password=models.CharField(max_length=20)

    def __str__(self):
        return self.email
    

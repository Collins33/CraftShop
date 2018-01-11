from django.db import models

# Create your models here.
class Artist(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    email=models.EmailField()

    #make class readable from shell
    def __str__(self):
        return self.first_name




class categories(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name    

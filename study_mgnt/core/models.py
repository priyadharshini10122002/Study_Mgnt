from django.db import models

# Create your models here.
class Study(models.Model):
    Name = models.CharField(max_length=20)
    Description =models.CharField(max_length=100)
    Phase=models.CharField(max_length=10)
    Sponser_Name=models.CharField(max_length=20)
    def __str__(self):
        return self.Sponser_Name 
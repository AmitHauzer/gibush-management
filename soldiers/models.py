from django.db import models

# Create your models here.
class Soldier(models.Model):
   
    name = models.CharField(max_length=50)
    soldier_status = models.CharField(max_length=50 , default='Waiting for Baror')

    def __str__(self) -> str:
        return f'{self.name}'
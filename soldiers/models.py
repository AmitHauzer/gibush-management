from django.db import models

# Create your models here.
class Soldier(models.Model):
   
    name = models.CharField(max_length=50)
    # status = models.TextChoices(value=STATUS)


    def __str__(self) -> str:
        return f'{self.name}'
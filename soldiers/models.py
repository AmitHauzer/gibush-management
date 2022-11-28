from django.db import models

# Create your models here.
class Soldier(models.Model):
    Soldier_SATUTS = {
        'Waiting for Shalishut':'Waiting for Shalishut',
        'Waiting for Baror':'Waiting for Baror',
        'Ready to run':'Ready to run',
        'Running':'Running',
        'After Baror':'After Baror', 
    }

    name = models.CharField(max_length=50)
    soldier_status = models.CharField(max_length=50 , default=f'{Soldier_SATUTS["Waiting for Shalishut"]}')

    def __str__(self) -> str:
        return f'{self.name}'
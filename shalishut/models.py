from django.db import models
from soldiers.models import Soldier


# Create your models here.
class Shalishut(models.Model):
    class ShalishutStatus(models.TextChoices):
        OPEN = 'Open', 'Open'
        DONE = 'Done', 'Done'
    class Profiletype(models.IntegerChoices):
        NINETY_SEVEN = 97, '97'
        EIGHTY_TWO = 82, '82'
        SEVENTY_TWO = 72, '72'
        
    soldier = models.OneToOneField(Soldier, max_length=50, on_delete=models.CASCADE)
    identity_num = models.CharField(max_length=9, null=True)
    firstname = models.CharField(max_length=20, null=True)
    lastname = models.CharField(max_length=20, null=True)
    city = models.CharField(max_length=50, null=True)
    profile = models.IntegerField(choices=Profiletype.choices, null=True)
    # kaba =
    # image = 
    shalishut_status = models.CharField(max_length=50, default=ShalishutStatus.OPEN, choices=ShalishutStatus.choices, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    def update_soldier_status(self):
        self.soldier.soldier_status = self.soldier.SoldierStatus.WAITING_FOR_CLINIC
        self.soldier.save()
        print(f'soldier status updated to: {self.soldier.soldier_status}.')



    def __str__(self) -> str:
        return f' IDF: {self.soldier.idf_num}, Name: {self.firstname} {self.lastname}, ID: {self.identity_num}, Soldier Status: {self.soldier.soldier_status}, City: {self.city}'
from django.db import models

# Create your models here.
class Soldier(models.Model):
    class SoldierStatus(models.TextChoices):
        WAITING_FOR_SHALISHUT = 'Waiting for Shalishut','Waiting for Shalishut'
        WAITING_FOR_CLINIC = 'Waiting for Clinic','Waiting for Clinic'
        WAITING_FOR_BAROR = 'Waiting for Baror','Waiting for Baror'
        READY_TO_RUN = 'Ready to run','Ready to run'
        RUNNING = 'Running','Running'
        AFTER_BAROR =  'After Baror','After Baror'
        MEDICALLY_DISQUALIFIED = 'Medically disqualified','Medically disqualified'
        ACTIVE = 'Active','Active'
        QUIT = 'Quit','Quit'
        PASS = 'Pass','Pass'


    idf_num = models.PositiveSmallIntegerField()
    soldier_status = models.CharField(max_length=50 , default=SoldierStatus.WAITING_FOR_SHALISHUT, choices=SoldierStatus.choices)

    def __str__(self) -> str:
        return f'IDF: {self.idf_num} - Soldier Status: {self.soldier_status}'
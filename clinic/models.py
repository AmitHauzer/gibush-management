from django.db import models
from soldiers.models import Soldier


# Create your models here.
class Clinic(models.Model):
    class ClinicStatus(models.TextChoices):
        FIT = 'Fit', 'Fit'
        UNFIT = 'Unfit', 'Unfit'
    
    def user_directory_path(instance, filename):
        pk = instance.soldier.id
        idf_num = instance.soldier.idf_num
        folder = f'IDF-{idf_num}_pk-{pk}'
        path = f'{folder}/{filename}'
        return path

    soldier = models.OneToOneField(Soldier, max_length=50, on_delete=models.CASCADE)
    health_declaration = models.FileField(upload_to=user_directory_path, max_length=254)
    clinic_status = models.CharField(max_length=50, default=ClinicStatus.FIT, choices=ClinicStatus.choices, editable=False)
    note = models.TextField(max_length=200, null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def update_soldier_status(self):
        if self.clinic_status == self.ClinicStatus.FIT:
            self.soldier.soldier_status = self.soldier.SoldierStatus.WAITING_FOR_BAROR    
        elif self.clinic_status == self.ClinicStatus.UNFIT:
            self.soldier.soldier_status = self.soldier.SoldierStatus.MEDICALLY_DISQUALIFIED
        self.soldier.save()
        print(f'soldier status updated to: {self.soldier.soldier_status}.')


    def __str__(self) -> str:
        return f'IDF: {self.soldier.idf_num}'
from django.db import models

from soldiers.models import Soldier

# Create your models here.
class BarOr(models.Model):
    baror_round = models.CharField(max_length=50 , unique=True)
    start_round_date = models.DateField(null=True, blank=True)
    soldiers = models.ManyToManyField(Soldier, through='BarorScore', through_fields=['baror_round','soldier'])
    
    
    def __str__(self) -> str:
        return f'{self.baror_round}'


class BarorScore(models.Model):
    baror_round = models.ForeignKey(BarOr, on_delete=models.CASCADE)
    soldier = models.ForeignKey(Soldier, on_delete=models.CASCADE)
    baror_score = models.DateField()

    def __str__(self) -> str:
        return f'{self.baror_round} - {self.soldier} - {self.baror_score}'
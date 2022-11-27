from django.db import models
from datetime import datetime, timezone
from soldiers.models import Soldier

# Create your models here.
class BarOr(models.Model):
    BAROR_SATUTS = {
        'Waiting for allocate':'Waiting for allocate',
        'Ready':'Ready',
        'Running':'Running',
        'Done':'Done', 
    }

    baror_round = models.CharField(max_length=50 , unique=True)
    start_round_date = models.DateTimeField(null=True, blank=True)
    stop_round_date = models.DateTimeField(null=True, blank=True)
    baror_status = models.CharField(max_length=20 , default=f'{BAROR_SATUTS["Waiting for allocate"]}')
    
    def set_start_time(self):
        # Adding start time and changing the status
        self.start_round_date = datetime.now(tz=timezone.utc)
        # self.baror_status = BarOr.BAROR_SATUTS['Running']
        self.baror_status = self.BAROR_SATUTS['Running']
        self.save()
        print(self)

    def set_stop_time(self):
        # Adding stop time and changing the status
        self.stop_round_date = datetime.now(tz=timezone.utc)
        self.baror_status = BarOr.BAROR_SATUTS['Done']
        self.save()
        print(self)
        print(f'{self.baror_round} has been finished')

    
    def __str__(self) -> str:
        return f"ROUND: {self.baror_round} - STATUS: {self.baror_status} - START TIME: {self.start_round_date} - STOP TIME:{self.stop_round_date}"


##################################################################################

class BarorScore(models.Model):
    baror_round = models.ForeignKey(BarOr, on_delete=models.CASCADE)
    soldier = models.ForeignKey(Soldier, on_delete=models.CASCADE)
    float_score = models.FloatField(max_length=200, null=True, blank=True)
    str_score = models.CharField(max_length=10, null=True, blank=True)

    def update_soldier_status_to_running(self):
        # self.soldier.soldier_status = Soldier.Soldier_SATUTS['Running']
        self.soldier.soldier_status = self.soldier.Soldier_SATUTS['Running']
        self.soldier.save()
        print(f'Soldier:{self.soldier.name} - Status: {self.soldier.soldier_status} ')

    def update_score(self):
        # calculate time
        end_time = datetime.now(tz=timezone.utc)
        start_time = self.baror_round.start_round_date
        result = end_time.timestamp() - start_time.timestamp()
        # save in db
        self.float_score = result
        self.str_score = datetime.fromtimestamp(result, tz=timezone.utc).strftime("%H:%M:%S:%f")[:-4]
        self.save()
        self.soldier.soldier_status = Soldier.Soldier_SATUTS['After Baror']
        self.soldier.save()
        print(self)




    def __str__(self) -> str:
        return f'{self.baror_round} - {self.soldier} - {self.float_score} - {self.str_score}'
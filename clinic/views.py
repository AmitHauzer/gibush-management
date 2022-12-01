from django.shortcuts import render
from django.http import HttpResponse
from soldiers.models import Soldier


# Create your views here.
def menu(request):
    soldiers_befor = Soldier.objects.filter(soldier_status=Soldier.SoldierStatus.WAITING_FOR_SHALISHUT)
    soldiers_after = Soldier.objects.exclude(soldier_status=Soldier.SoldierStatus.WAITING_FOR_SHALISHUT)
    return render(request, 'clinic_menu.html',{'soldiers':{'before':soldiers_befor, 'after':soldiers_after}})

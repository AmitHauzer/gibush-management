from django.shortcuts import render
from django.http import HttpResponse
from soldiers.models import Soldier


def menu(request):
    # A dictionary which ordered by all the statuses
    status = {}
    for s in Soldier.SoldierStatus:
        key = str(s).upper().replace(' ','_')
        status[key]=Soldier.objects.filter(soldier_status=s)
    return render(request,'commander_menu.html', {'status':status})
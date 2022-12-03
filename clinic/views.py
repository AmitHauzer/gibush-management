from django.shortcuts import redirect, render
from django.http import HttpResponse
from soldiers.models import Soldier
from clinic.models import Clinic
from django.contrib import messages
from django.db.models import Q


# Create your views here.
def menu(request):
    soldiers_befor = Soldier.objects.filter(soldier_status=Soldier.SoldierStatus.WAITING_FOR_CLINIC)
    soldiers_after = Soldier.objects.exclude(Q(soldier_status=Soldier.SoldierStatus.WAITING_FOR_CLINIC) | Q(soldier_status=Soldier.SoldierStatus.WAITING_FOR_SHALISHUT))
    return render(request, 'clinic_menu.html',{'soldiers':{'before':soldiers_befor, 'after':soldiers_after}})


def search(request):
    search_req = request.GET.get('search')
    soldiers = Soldier.objects.filter(Q(shalishut__firstname__istartswith=search_req) | Q(shalishut__lastname__istartswith=search_req) | Q(idf_num__icontains=search_req) | Q(shalishut__identity_num__istartswith=search_req))
    soldiers_befor = soldiers.filter(soldier_status=Soldier.SoldierStatus.WAITING_FOR_CLINIC)
    soldiers_after = soldiers.exclude(Q(soldier_status=Soldier.SoldierStatus.WAITING_FOR_CLINIC) | Q(soldier_status=Soldier.SoldierStatus.WAITING_FOR_SHALISHUT))
    return render(request, 'clinic_menu.html',{'soldiers':{'before':soldiers_befor, 'after':soldiers_after}})


def update_soldier(request, pk):
    soldier = Soldier.objects.get(id=pk)
    if request.method == 'POST':
        file = request.FILES.get('health_declaration')
        # TODO: add verification to the file
        note = request.POST.get('note')
        medial_condition = request.POST.get('medial_condition')
        clinic = Clinic(soldier=soldier, health_declaration=file, clinic_status=medial_condition, note=note)
        clinic.save()
        # change soldier status
        clinic.update_soldier_status()
        return redirect('clinic:menu-clinic')

    return render(request, 'update_clinic_soldier.html',{'status':Clinic.ClinicStatus, 'soldier':soldier})
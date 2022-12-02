from django.shortcuts import render, redirect
from soldiers.models import Soldier
from shalishut.models import Shalishut
from django.contrib import messages
from django.db.models import Q

# Create your views here.
def menu(request):
    soldiers_befor = Soldier.objects.filter(soldier_status=Soldier.SoldierStatus.WAITING_FOR_SHALISHUT)
    soldiers_after = Soldier.objects.exclude(soldier_status=Soldier.SoldierStatus.WAITING_FOR_SHALISHUT)
    return render(request, 'shalishut_menu.html',{'soldiers':{'before':soldiers_befor, 'after':soldiers_after}})


def add_soldier(request):
    if request.method == 'POST':
        idf_num = request.POST.get('idf_num')
        already_exist = Soldier.objects.filter(idf_num=idf_num)
        if already_exist:
            messages.error(request, 'Gibush number already exist.')
        else:
            try:
                soldier = Soldier(idf_num=idf_num)
                soldier.save()
                shalishut = Shalishut(soldier=soldier, profile=0)
                shalishut.save()
                messages.success(request, f'Soldier added successfully')
                return redirect('shalishut:menu-shalishut')
            except Exception as ex:
                messages.error(request, f'ERROR! {str(ex)}')
    return render(request, 'add_soldier.html')


def update_soldier(request, pk):
    shalishut=Shalishut.objects.get(soldier=pk)
    # soldier = Soldier.objects.get(id=pk)
    if request.method == 'POST':
        shalishut.identity_num = request.POST.get('identity_num')
        shalishut.firstname = request.POST.get('first_name')
        shalishut.lastname = request.POST.get('last_name')
        shalishut.city = request.POST.get('city')
        shalishut.profile = request.POST.get('profile')
        try:
            shalishut.shalishut_status = Shalishut.ShalishutStatus.DONE
            shalishut.save()
            # update soldier status
            shalishut.soldier.soldier_status = shalishut.soldier.SoldierStatus.WAITING_FOR_CLINIC
            shalishut.soldier.save()
            messages.success(request, f'Soldier updated successfully')
            return redirect('shalishut:menu-shalishut')
        except Exception as ex:
                messages.error(request, f'ERROR! {str(ex)}')
    return render(request, 'update_soldier.html',{'profiles':Shalishut.Profiletype, 'shalishut':shalishut})


def search(request):
    search_req = request.GET.get('search')
    soldiers = Soldier.objects.filter(Q(shalishut__firstname__istartswith=search_req) | Q(shalishut__lastname__istartswith=search_req) | Q(idf_num__icontains=search_req) | Q(shalishut__identity_num__istartswith=search_req))
    soldiers_befor = soldiers.filter(soldier_status=Soldier.SoldierStatus.WAITING_FOR_SHALISHUT)
    soldiers_after = soldiers.exclude(soldier_status=Soldier.SoldierStatus.WAITING_FOR_SHALISHUT)
    return render(request, 'shalishut_menu.html',{'soldiers':{'before':soldiers_befor, 'after':soldiers_after}})
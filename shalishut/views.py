from django.shortcuts import render, redirect
from soldiers.models import Soldier
from django.contrib import messages

# Create your views here.
def menu(request):
    soldiers = Soldier.objects.all().filter(soldier_status=Soldier.Soldier_SATUTS['Waiting for Shalishut'])
    return render(request, 'shalishut_menu.html',{'soldiers':soldiers})


def add_soldier(request):
    if request.method == 'POST':
        idf_num = request.POST.get('idf_num')
        soldier_name = request.POST.get('soldier_name')
        error = False
        already_exist = Soldier.objects.filter(idf_num=idf_num)
        if already_exist:
            messages.error(request, 'Gibush number already exist.')
            error = True
        if error is False:
            try:
                soldier = Soldier(name=soldier_name, idf_num=idf_num)
                soldier.save()
                messages.success(request, f'Soldier added successfully')
                return redirect('shalishut:menu-shalishut')
            except Exception as ex:
                messages.error(request, f'ERROR! {str(ex)}')
    return render(request, 'add_soldier.html')


# def update_soldier(request, pk):
#     soldier = Soldier.objects.get(id=pk)
#     if request.method == 'POST':
#         # try update
#         # change status 
    
     
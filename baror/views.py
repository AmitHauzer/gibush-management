from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import BarOr, BarorScore
from soldiers.models import Soldier
from colorama import Fore


def list_of_barors(request):
    barors = BarOr.objects.all()
    return render(request, 'list_of_barors.html', {'barors':barors})



def add_baror(request):
    barors_counter = BarOr.objects.count()
    try:
        baror = BarOr(baror_round=f'BarOr {barors_counter+1}')
        baror.save()
        messages.success(request, "Round added successfully" )
    except Exception as ex:
        messages.error(request, f'ERROR! {str(ex)}')
    finally:
        return redirect('barors:all-barors')



def edit_baror(request, pk):
    print(pk)
    baror = BarOr.objects.get(id=pk)
    soldiers = Soldier.objects.filter(soldier_status='Waiting for Baror')
    return render(request, 'edit_baror.html', {'baror':baror,'soldiers':soldiers})



def baror_is_ready(request, pk):
    # Get baror
    baror = BarOr.objects.get(id=pk)
    # Change status
    baror.baror_status = baror.BarorStatus.READY
    baror.save()
    # save
    print(f'{baror.baror_round} is ready')
    return redirect('barors:all-barors')



def add_soldier_to_round(request):
    # Get params (POST)
    baror_id = request.POST.get('pk')
    soldier_id = request.POST.get('soldier_id')
    print(f'Baror ID: {baror_id}')                          # not necessary
    print(f'Soldier ID: {soldier_id}')                      # not necessary
    # Get Objects
    soldier = Soldier.objects.get(id=soldier_id)
    baror = BarOr.objects.get(id=baror_id)
    # Add to BarorScore
    baror_score = BarorScore(baror_round=baror, soldier=soldier)
    baror_score.save()
    # Update soldier's status
    baror_score.update_soldier_status_to_running()
    print(f'Baror Score: {baror_score}')
    return redirect('barors:edit-baror',pk=baror_id)



def start_baror_page(request, pk):
    # Get baror
    baror = BarOr.objects.get(id=pk)
    barorscores = BarorScore.objects.all().filter(baror_round=pk).order_by('float_score')
    if request.method == 'POST':
        # add baror start date and update status
        baror.set_start_time()
        # update soldiers' status
        for score in barorscores:
            score.update_soldier_status_to_running()
    return render(request, 'baror_round.html', {'baror':baror, 'barorscores':barorscores})



def manage_running_round(request,pk):
    # Get data
    if request.method == 'POST':
        soldier_id = request.POST.get('soldier_id')
        barorscore = BarorScore.objects.get(baror_round=pk, soldier=soldier_id)
        barorscore.update_score()
        
        # check if baror has been finished
        barorscores = BarorScore.objects.all().filter(baror_round=pk, float_score=None)
        if not barorscores:
            baror = BarOr.objects.get(id=pk)
            baror.set_stop_time()
            return redirect('barors:all-barors')
    return redirect('barors:start-baror', pk=pk)






###########################################################################

# def delete_baror(request, pk):
#     # only admin
#     # if not request.user.is_staff:
#     #     return HttpResponse('YOU ARE Not allowed to delete books')
#     try:
#         baror = BarOr.objects.get(id=pk)
#         baror_name = baror.baror_round
#         messages.success(request, f'{baror_name} deleted!')
#         return redirect('baror:all-barors')
#     except Exception as ex:
#         messages.error(request, f'ERROR! {str(ex)}')

#     return HttpResponse(f'delete baror')


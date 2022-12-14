from django.shortcuts import render
from django.http import HttpResponse
from soldiers.models import Soldier
from baror.models import BarorScore
from user_management.decorators import allowed_users, login_required


@login_required
def menu(request):
    # A dictionary which ordered by all the statuses
    status = {}
    for s in Soldier.SoldierStatus:
        key = str(s).upper().replace(' ','_')
        status[key]=Soldier.objects.filter(soldier_status=s)
    return render(request,'commander_menu.html', {'status':status})


@allowed_users(allowed_roles=['Commander'])
def acceptance_criteria(request):
    # Get data
    all_baror_score = BarorScore.objects.exclude(float_score=None).order_by('float_score')
    after_baror_status = Soldier.objects.filter(soldier_status=Soldier.SoldierStatus.AFTER_BAROR)
    active_status = Soldier.objects.filter(soldier_status=Soldier.SoldierStatus.ACTIVE)
    quit_status = Soldier.objects.filter(soldier_status=Soldier.SoldierStatus.QUIT)

    if request.method == 'POST':
        limit = request.POST.get('limit')
        print(f'counter: {limit}')
        if limit:
            counter = 1
            for score in all_baror_score:
                if counter <= int(limit):
                    # until the counter is done, status is active
                    print(f'{counter}.  {score.float_score}')
                    score.soldier.soldier_status = Soldier.SoldierStatus.ACTIVE
                    score.soldier.save()
                    counter += 1
                else:
                    # after, status Quit.
                    print(f'{score.float_score}')
                    score.soldier.soldier_status = Soldier.SoldierStatus.QUIT
                    score.soldier.save()
                
        elif not limit:      
        # else:
            for score in all_baror_score:
                # change status to 'after baror' and restart
                score.soldier.soldier_status = Soldier.SoldierStatus.AFTER_BAROR
                score.soldier.save()
                print('DONE')
    
    return render(request, 'acceptance_criteria.html', {'all_baror_score':all_baror_score, 'active_status':active_status, 'quit_status':quit_status, 'after_baror_status':after_baror_status})
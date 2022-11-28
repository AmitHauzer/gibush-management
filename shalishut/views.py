from django.shortcuts import render, redirect

from soldiers.models import Soldier

# Create your views here.
def menu(request):
    soldiers = Soldier.objects.all()
    return render(request, 'shalishut_menu.html',{'soldiers':soldiers})
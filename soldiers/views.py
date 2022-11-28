from django.shortcuts import render
from soldiers.models import Soldier


# Create your views here.
def all_soldiers(request):
    soldiers = Soldier.objects.all()
    return render(request, 'soldiers.html',{'soldiers':soldiers})


def single_soldier(request, pk):
    soldier = Soldier.objects.get(id=pk)
    return render(request, 'single_soldier.html',{'soldier':soldier})




def home_page(request):
    return render(request, 'home.html')
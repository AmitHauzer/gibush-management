from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from .decorators import allowed_users, login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse


from django.contrib.auth.forms import UserCreationForm, UserChangeForm,AuthenticationForm, SetPasswordForm, AdminPasswordChangeForm

@allowed_users(allowed_roles=['Commander'])
def menu(request):
    active_users = User.objects.filter(is_active=True)
    inactive_users = User.objects.exclude(is_active=True)
    return render(request, 'users_menu.html', {'users':{'active':active_users, 'inactive':inactive_users}})


def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home-page')
        else:
            messages.error(request, "Your username and password didn't match. Please try again.")
    form = AuthenticationForm(request.user)
    return render(request, 'login.html', {'form':form})




@login_required
def home_page(request):
    return render(request, 'home.html')
# to get path 'home/'
def edit_home_path(request):
    return redirect('home-page')

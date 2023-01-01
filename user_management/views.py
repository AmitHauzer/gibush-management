from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from .decorators import allowed_users, login_required
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.http import HttpResponse


from django.contrib.auth.forms import UserCreationForm, UserChangeForm,AuthenticationForm, SetPasswordForm, AdminPasswordChangeForm

@allowed_users(allowed_roles=['Commander'])
def menu(request):
    active_users = User.objects.filter(is_active=True)
    inactive_users = User.objects.exclude(is_active=True)
    return render(request, 'users_menu.html', {'users':{'active':active_users, 'inactive':inactive_users}})


@allowed_users(allowed_roles=['Commander'])
def add_user(request): 
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST.get('username')
            messages.success(request, f"The user {username} has been added successfully" )
            return redirect("user_management:menu-users")
        else:
            form_error_handling(request, form)
    return render(request, 'add_user.html', {'form':form})


@allowed_users(allowed_roles=['Commander'])
def edit_user(request, pk):
    user = User.objects.get(id=pk) 
    form = UserChangeForm()
    if request.method == 'POST':
        form = UserChangeForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST.get('username')
            messages.success(request, f"The user {username} has been edited successfully" )
            return redirect("user_management:menu-users")
        else:
            form_error_handling(request, form)
    return render(request, 'edit_user.html', {'form':form})


def login_page(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You logged in as {username}.")
                return redirect('home-page')
            else:
                messages.error(request, "Your username and password didn't match. Please try again.")
        else:
            form_error_handling(request, form)
    return render(request, 'login.html', {'form':form})


@login_required
def home_page(request):
    return render(request, 'home.html')
# to get path 'home/'
def edit_home_path(request):
    return redirect('home-page')


def logout_page(request):
	logout(request)
	messages.info(request, "You have logged out.") 
	return redirect("home-page")


def form_error_handling(request, form):
     for key in form.errors.keys():
        for error in form.errors.get(key):
            messages.error(request, f'ERROR! {error}')
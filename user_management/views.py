from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from soldiers.models import Soldier
from .decorators import allowed_users, login_required
from django.contrib.auth.models import User, Group
from django.db.models import Q
from django.contrib import messages


from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

@allowed_users(allowed_roles=['Commander'])
def menu(request):
    all_users = User.objects.all()
    inactive_users = User.objects.exclude(is_active=True)
    return render(request, 'users_menu.html', {'users': {'all': all_users, 'inactive': inactive_users}, 'search_url': 'user_management:search-users'})


@allowed_users(allowed_roles=['Commander'])
def add_user(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST.get('username')
            messages.success(
                request, f"The user {username} has been added successfully")
            return redirect("user_management:menu-users")
        else:
            form_error_handling(request, form)
    return render(request, 'add_user.html', {'form': form})


@allowed_users(allowed_roles=['Commander'])
def edit_user(request, pk):
    current_user = request.user
    user_edit = User.objects.get(id=pk)
    groups = Group.objects.all()
    if user_edit.is_superuser and not current_user.is_superuser:
        messages.error(request, f"Sorry, only the admin can edit a superuser.")
        return redirect("user_management:menu-users")
    if request.method == 'POST':
        username_edit = request.POST.get('username')
        firstname_edit = request.POST.get('first_name')
        lastname_edit = request.POST.get('last_name')
        email_edit = request.POST.get('email')
        is_active_edit = request.POST.get('is_active')
        groups_edit = request.POST.getlist('groups')
        try:
            # Is active?
            if current_user.username != user_edit.username:
                if is_active_edit == 'on':
                    user_edit.is_active = True
                    messages.success(request, f"The user {user_edit.username} has been activated.")
                else:
                    user_edit.is_active = False
                    messages.warning(request, f"The user {user_edit.username} has been deactivated.")
            elif is_active_edit != 'on':
                messages.error(request, f"You can't deactivate your account.")

            # Change username:
            if user_edit.username != username_edit:
                user_edit.username = username_edit

            # Personal details:
            if firstname_edit:
                user_edit.first_name = firstname_edit
            else:
                user_edit.first_name = ''
            if lastname_edit:
                user_edit.last_name = lastname_edit
            else:
                user_edit.last_name = ''
            if email_edit:
                user_edit.email = email_edit
            else:
                user_edit.email = ''

            # Save
            user_edit.save()

            # Groups
            user_edit.groups.set(groups_edit)

            messages.success(
                request, f"The user {username_edit} has been edited successfully")
            return redirect("user_management:menu-users")
        except Exception as ex:
            messages.error(request, f"ERROR! {ex}")
    return render(request, 'edit_user.html', {'user_edit': user_edit, 'groups': groups})


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
                messages.error(
                    request, "Your username and password didn't match. Please try again.")
        else:
            form_error_handling(request, form)
    return render(request, 'login.html', {'form': form})


@login_required
def search(request):
    search_req = request.GET.get('search')
    all_users = User.objects.filter(
        Q(username__istartswith=search_req) |
        Q(first_name__istartswith=search_req) |
        Q(last_name__istartswith=search_req)
    )
    inactive_users = all_users.exclude(is_active=True)
    return render(request, 'users_menu.html', {'users': {'all': all_users, 'inactive': inactive_users}, 'search_url': 'user_management:search-users'})


# @login_required       # this is in comment for the welcome page
def home_page(request):
    status = {}
    for s in Soldier.SoldierStatus:
        key = str(s).upper().replace(' ', '_')
        status[key] = Soldier.objects.filter(soldier_status=s)
    return render(request, 'home.html', {'status': status})


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

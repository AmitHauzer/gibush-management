from django.urls import path
from . import views

app_name = 'user_management'
urlpatterns = [
    # Users
    path('', views.menu, name='menu-users'),
    path('adduser/', views.add_user, name='add-user-users'),
    path('edituser/<pk>', views.edit_user, name='edit-user-users'),
    path('search/', views.search, name='search-users'),
    path('login/', views.login_page, name='login-page'),
    path('logout/', views.logout_page, name='logout-page'),
    
    
]
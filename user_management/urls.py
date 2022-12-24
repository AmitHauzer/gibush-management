from django.urls import path
from . import views

app_name = 'user_management'
urlpatterns = [
    # Users
    path('', views.menu, name='menu-users'),
    path('adduser/', views.menu, name='add-user-users'),
    path('login/', views.login_page, name='login-page'),
    
    
]
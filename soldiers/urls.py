from django.urls import path, include
from . import views

app_name = 'soldiers'
urlpatterns = [
    path('', views.all_soldiers, name='all-soldiers'),
    path('<pk>/', views.single_soldier, name='single-soldier'),
    
]
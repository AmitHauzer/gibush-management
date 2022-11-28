from django.urls import path
from . import views

app_name = 'shalishut'
urlpatterns = [
    path('', views.menu, name='menu-shalishut'),
]
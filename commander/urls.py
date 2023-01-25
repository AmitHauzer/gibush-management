from django.urls import path
from . import views

app_name = 'commander'
urlpatterns = [
    path('', views.menu, name='menu-commander'),
    path('AcceptanceCriteria/', views.acceptance_criteria, name='acceptance-criteria-commander')
]
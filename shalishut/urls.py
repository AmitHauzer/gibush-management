from django.urls import path
from . import views

app_name = 'shalishut'
urlpatterns = [
    path('', views.menu, name='menu-shalishut'),
    path('addsoldier/', views.add_soldier, name='add-soldier-shalishut'),
    path('<pk>/updatesoldier', views.update_soldier, name='update-soldier-shalishut'),
    path('search/', views.search, name='search-shalishut'),
]
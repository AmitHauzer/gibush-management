from django.urls import path, include
from . import views

app_name = 'clinic'
urlpatterns = [
    path('', views.menu, name='menu-clinic'),
    path('search/', views.search, name='search-clinic'),
    # path('addsoldier/', views.add_soldier, name='add-soldier-shalishut'),
    path('<pk>/updatesoldier', views.update_soldier, name='update-soldier-clinic'),
    
]
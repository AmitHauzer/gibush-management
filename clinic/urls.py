from django.urls import path
from . import views

app_name = 'clinic'
urlpatterns = [
    path('', views.menu, name='menu-clinic'),
    path('search/', views.search, name='search-clinic'),
    path('<pk>/updatesoldier', views.update_soldier, name='update-soldier-clinic'), 
]
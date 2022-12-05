from django.urls import path
from . import views

app_name = 'commander'
urlpatterns = [
    path('', views.menu, name='menu-commander'),
    # path('addsoldier/', views.add_soldier, name='add-soldier-commander'),
    # path('<pk>/updatesoldier', views.update_soldier, name='update-soldier-commander'),
    # path('search/', views.search, name='search-commander'),
]
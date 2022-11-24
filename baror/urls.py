from django.urls import path, include
from . import views

app_name = 'barors'
urlpatterns = [
    path('', views.list_of_barors, name='all-barors'),
    path('addround/', views.add_baror_round, name='add-baror'),
    path('<pk>/editround/', views.edit_baror, name='edit-baror'),
    path('addsoldier/', views.add_soldier_to_round, name='add-soldier-to-round'),
    path('<pk>/barorReady/', views.baror_is_ready, name='baror-is-ready'),
]





# Old:
# path('createbaror/', views.create_baror, name='create-baror'),
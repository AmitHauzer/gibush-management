from django.urls import path
from . import views

app_name = 'barors'
urlpatterns = [
    path('', views.list_of_barors, name='all-barors'),
    path('addround/', views.add_baror, name='add-baror'),
    path('<pk>/editround/', views.edit_baror, name='edit-baror'),
    path('addsoldier/', views.add_soldier_to_round, name='add-soldier-to-round'),
    path('<pk>/barorReady/', views.baror_is_ready, name='baror-is-ready'),
    path('<pk>/manageround/', views.start_baror_page, name='start-baror'),
    path('<pk>/manageround/soldierendthebaror/', views.manage_running_round, name='manage-soldier-in-round'),
]
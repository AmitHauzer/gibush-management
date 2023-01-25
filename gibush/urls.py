"""gibush URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from user_management import views
from django.conf.urls.static import static
from . import settings




urlpatterns = [
    path('admin/', admin.site.urls),
    # Home page
    path('', views.edit_home_path, name='edit-home-page'),
    path('home/', views.home_page, name='home-page'),
    # Apps
    path('soldiers/', include('soldiers.urls')),
    path('barors/', include('baror.urls')),
    path('shalishut/', include('shalishut.urls')),
    path('clinic/', include('clinic.urls')),
    path('commander/', include('commander.urls')),
    path('users/', include('user_management.urls')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
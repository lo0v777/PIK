"""
URL configuration for hack project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from apphack import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.reg, name='reg'),
    path('/', views.reg2, name='reg2'),
    path('main', views.main, name='main'),
    path('profile', views.profile, name='profile'),
    path('1', views.first, name='first'),
    path('2', views.second, name='second'),
    path('3', views.third, name='third'),
]

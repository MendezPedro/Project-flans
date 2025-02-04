"""
URL configuration for onlyflans project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from web import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.inicio, name='inicio'),  
    path('acerca/', views.about, name='acerca'), 
    path('bienvenido/', views.welcome, name='bienvenido'), 
    path('contacto', views.contacto, name='contacto'), 
    path('exito/', views.exito, name='exito'), 

    path('review/', views.review_view, name='review'),
    path('review/success/', views.review_success_view, name='review_success'),
    path('reviews/', views.review_list, name='review_list'),
]

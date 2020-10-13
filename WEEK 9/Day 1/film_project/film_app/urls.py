from django.contrib import admin
from django.urls import path, include
from . import views
from .views import AddDirector, Profile

urlpatterns = [
    path('home/', views.home, name='home'),
    path('profile/<pk>', Profile.as_view(), name='profile'),
    path('add_film/', views.add_film, name='add_film'),
    path('add_director/', AddDirector.as_view(), name='add_director'),
]

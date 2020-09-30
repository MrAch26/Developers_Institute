from django.urls import path
from . import views

urlpatterns = [
    path('', views.search_person),
    path('done/', views.search_person)
]
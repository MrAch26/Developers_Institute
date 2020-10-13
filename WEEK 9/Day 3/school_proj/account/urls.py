from django.urls import path, include
from . import views

urlpatterns = [
    path('signup/',views.UserSignUp.as_view(),name="signup"),
]
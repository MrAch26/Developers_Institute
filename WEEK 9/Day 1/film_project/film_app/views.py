from django.shortcuts import render
from django.views.generic import View, DetailView
# Create your views here.

# class FilmView(View):


def home(request):
    return render(request, 'homepage.html')
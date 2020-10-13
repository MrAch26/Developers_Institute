from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import View, DetailView, CreateView

from film_app.forms import AddFilmForm, AddDirectorForm
from film_app.models import Director, Film


def home(request):
    film = Film.objects.all()
    return render(request, 'homepage.html', {'film': film})

class Profile(DetailView):
    model = User
    template_name = 'profile.html'


def add_film(request):
    if request.method == 'GET':
        form = AddFilmForm()
        return render(request, 'film/add_film.html', {'form': form})

    if request.method == 'POST':
        form = AddFilmForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddFilmForm()
    return render(request, 'film/add_film.html', {'form': form})


class AddDirector(CreateView):
    model = Director
    form_class = AddDirectorForm
    template_name = 'director/add_director.html'
    success_url = reverse_lazy('home')

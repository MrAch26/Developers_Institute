from django.shortcuts import render, redirect, reverse
from django.views.generic import CreateView
from .forms import SignupForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from students.models import Profile

class UserSignUp(CreateView):
    template_name = "registration/signup.html"
    model = User
    form_class = SignupForm
    success_url = 'home'
    failed_message = "The User couldn't be added"


    def form_valid(self, form):
        super().form_valid(form)   

        user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
        
        Profile.objects.create(user=user, age=form.cleaned_data['age'])

        if user:
            login(self.request, user)
            
        return redirect(reverse(self.get_success_url()))
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import ContactFrom, SnippetForm

from django.views.generic import ListView, DetailView, CreateView
from django.views import View

from .models import Snippet


def contact(request):
    if request.method == 'POST':
        form = ContactFrom(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']

            print(name)
    else:
        form = ContactFrom()

    context = {'form': form}
    return render(request, 'form.html', context)


class AddSnippet(CreateView):
    model = Snippet
    form_class = SnippetForm
    template_name = 'form1.html'
    success_url = reverse_lazy('snippet')


class SnippetView(ListView):
    model = Snippet
    template_name = 'display_forms.html'


class SnippetDetail(DetailView):
    model = Snippet
    template_name = 'display_detail.html'
    

# class SnippetDetailView(View):
#
#     def get(self, request):
#         form = SnippetForm
#         return render(request, 'form1.html', {'form': form})
#
#     def post(self, request):
#         form = SnippetForm(request.POST)
#         if form.is_valid():
#             form.save()
#             print("VALID")
#
#         return redirect('home')

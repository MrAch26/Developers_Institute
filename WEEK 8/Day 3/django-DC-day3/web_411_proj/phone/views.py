from django.shortcuts import render, redirect
from .forms import SearchForm
from .models import Person


# def home(request):
#     form = SearchForm()
#     context = {
#         "form": form
#     }
#     return render(request, 'home.html', context)


def search_person(request):
    if request.method == 'GET':
        form = SearchForm()
        return render(request, 'home.html', {'form': form})

    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            person = Person.objects.filter(
                name__icontains=form.cleaned_data["name"],
                phone_number__icontains=form.cleaned_data['phone_number']
            )

            context = {
                'Person': person
            }
            print(person)
            return render(request, 'searchDone.html', context)

    else:
        form = SearchForm()

        context = {
            'form': form
        }

    return render(request, 'home.html', context)

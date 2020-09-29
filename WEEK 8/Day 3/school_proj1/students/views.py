from django.shortcuts import render
from .models import Student, Pet

# Create your views here.

#VIEW
def home(request):

    # Calling the MODEL and asking for data
    students = Student.objects.all()
    pets = Pet.objects.all()

    context = {
        "students": students,
        "pets": pets
    }

    # Calling the TEMPLATE and asking for an html page to be built
    html = render(request, 'home.html', context)

    return html

    
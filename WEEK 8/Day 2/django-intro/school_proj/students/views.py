from django.shortcuts import render
from .models import Student, Pet
# Create your views here.
def home(request):

    # new_student = Student(first_name="Dandoune")
    # new_student.save()

    students = Student.objects.all()
    pets = Pet.objects.all()

    context = {
        "students": students,
        "pets": pets
    }

    return render(request, 'home.html', context)



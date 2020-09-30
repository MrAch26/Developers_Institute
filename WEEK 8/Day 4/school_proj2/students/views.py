from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Student, Pet, Profile
from .forms import AddStudentForm

# Create your views here.

#VIEW
def home(request):
    return render(request, 'home.html')


def students(request):

    # Calling the MODEL and asking for data
    students = Student.objects.all().order_by('profile','last_name')
    pets = Pet.objects.all()

    context = {
        "students": students,
        "pets": pets,
        "default_profile": "https://bit.ly/30jDurU"
    }

    # Calling the TEMPLATE and asking for an html page to be built
    html = render(request, 'students.html', context)

    return html


def add_student(request):


    if request.method == 'GET':
        form = AddStudentForm()
        return render(request, 'add_student.html', {'form' : form})


    if request.method == 'POST':
        form = AddStudentForm(request.POST)

        if form.is_valid():

            profile = Profile.objects.create(
                major=form.cleaned_data['major'], 
                minor=form.cleaned_data['minor'], 
                picture=form.cleaned_data['picture'], 
            )

            Student.objects.create(
                first_name = form.cleaned_data['first_name'],
                last_name = form.cleaned_data['last_name'],
                profile = profile
            )

            return redirect('students')
        


        





    
    
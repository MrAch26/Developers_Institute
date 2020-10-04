from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from .models import Student, Pet, Profile
from .forms import AddStudentForm

# Create your views here.

#VIEW
def home(request):
    return render(request, 'home.html')


def students_list(request):

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
        form.sayHi()
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
        
        else:
            return render(request, 'add_student.html', {'form' : form})
        


def student_details(request, id):
    # student = Student.objects.get(id=id)
    student = get_object_or_404(Student, id=id)


    return render(request, 'student-details.html', {"student": student})   
    

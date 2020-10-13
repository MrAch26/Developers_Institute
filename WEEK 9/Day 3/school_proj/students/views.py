from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from .models import *
from .forms import AddStudentForm, SubjectForm
from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views import View
from django.views.generic import ListView, DetailView, CreateView, YearArchiveView

from time import sleep

# Create your views here.


class SubjectList(LoginRequiredMixin, ListView):
    model = Subject
    template_name = 'subjects/subject_list.html'


class SubjectDetails(DetailView):
    model = Subject       
    template_name = 'subjects/subject_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class AddSubject(CreateView):
    model = Subject
    form_class = SubjectForm
    template_name = 'subjects/subject_add.html'
    success_url = reverse_lazy('subject-list')
    

#VIEW
def home(request):
    return render(request, 'home.html')


@login_required
def students_list(request):

    # Calling the MODEL and asking for data
    students = Student.objects.all().order_by('last_name')
    pets = Pet.objects.all()

    context = {
        "students": students,
        "pets": pets,
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
        
        else:
            return render(request, 'add_student.html', {'form' : form})
        


def student_details(request, id):
    # student = Student.objects.get(id=id)
    student = get_object_or_404(Student, id=id)

    return render(request, 'student-details.html', {"student": student})   
    
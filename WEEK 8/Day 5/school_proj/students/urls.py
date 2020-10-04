from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('students/', views.students_list, name='students'),
    path('students/add', views.add_student, name='students-add'),
    path('students/<int:id>', views.student_details, name='students-details')

]
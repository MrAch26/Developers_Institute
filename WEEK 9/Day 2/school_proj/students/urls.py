from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('subjects/', views.SubjectList.as_view(), name='subject-list'),
    path('subject/<int:pk>', views.SubjectDetails.as_view(), name='subject-details'),
    path('subjects/add', views.AddSubject.as_view(), name='subject-add'),

    path('students/', views.students_list, name='students'),
    path('students/add', views.add_student, name='students-add'),
    path('students/<int:id>', views.student_details, name='students-details')
]
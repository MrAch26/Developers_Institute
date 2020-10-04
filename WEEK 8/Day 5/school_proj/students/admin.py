from django.contrib import admin
from .models import Student, Pet, Profile

# Register your models here.
admin.site.register(Student)
admin.site.register(Pet)
admin.site.register(Profile)
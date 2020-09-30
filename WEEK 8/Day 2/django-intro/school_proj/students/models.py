from django.db import models

# Create your models here.

class Profile(models.Model):
    major = models.CharField(max_length=30,
        null=True)
    minor = models.CharField(max_length=30, null=True)
    github = models.URLField(max_length=200, null=True)

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=40)
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"



class Pet(models.Model):
    name = models.CharField(max_length=30)
    breed = models.CharField(max_length=30)
    owner = models.ForeignKey(Student, on_delete=models.CASCADE)  # Many to One

    def __str__(self):
        return f"{self.name}"
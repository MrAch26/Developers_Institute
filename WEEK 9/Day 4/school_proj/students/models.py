from django.db import models
from django.contrib.auth.models import User

class Subject(models.Model):
    name = models.CharField(max_length=30)
    textbook = models.CharField(max_length=30)
    class_room = models.IntegerField()
    
    def __str__(self):
        return self.name


class Profile(models.Model):
    age = models.IntegerField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.user}"


class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def sayHi(self):
        return f"Hi, my name is {self.first_name}, and I'm a {self.__class__.__name__.lower()}"



class Pet(models.Model):
    name = models.CharField(max_length=30)
    breed = models.CharField(max_length=30)
    owner = models.ForeignKey(Student, on_delete=models.CASCADE)  # Many to One

    def __str__(self):
        return f"{self.name}"

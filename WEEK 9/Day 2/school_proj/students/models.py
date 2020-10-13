from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=30)
    textbook = models.CharField(max_length=30)
    class_room = models.IntegerField()
    
    def __str__(self):
        return self.name


class Profile(models.Model):
    major = models.CharField(max_length=30, null=True)
    minor = models.CharField(max_length=30, null=True)
    picture = models.URLField(max_length=200, null=True)

    def __str__(self):
        return f"I'm majoring in {self.major}"


class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, null=True)
    
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

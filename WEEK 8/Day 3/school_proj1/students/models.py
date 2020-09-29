from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Pet(models.Model):
    name = models.CharField(max_length=30)
    breed = models.CharField(max_length=30)
    owner = models.ForeignKey(Student, on_delete=models.CASCADE)  # Many to One

    def __str__(self):
        return f"{self.name}"
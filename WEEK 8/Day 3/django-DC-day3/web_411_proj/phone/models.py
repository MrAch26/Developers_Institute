from django.db import models

# Create your models here
from phonenumber_field.modelfields import PhoneNumberField


class Person(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = PhoneNumberField(blank=True)
    address = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"

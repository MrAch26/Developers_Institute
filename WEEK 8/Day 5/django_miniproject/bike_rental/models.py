from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=26)
    last_name = models.CharField(max_length=26)
    email = models.EmailField(max_length=26)
    phone_number = models.CharField(max_length=26)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=26)
    country = models.CharField(max_length=26)


TYPE_CHOICES = [('b', 'Bike'), ('c', 'Car'), ('s', 'Scooter')]
class VehicleType(models.Model):
    name = models.CharField(max_length=10, choices=TYPE_CHOICES, default='b')


SIZE_CHOICES = [('s', 'Small'), ('m', 'Medium'), ('l', 'Large')]
class VehicleSize(models.Model):
    name = models.CharField(max_length=10, choices=SIZE_CHOICES, default='s')


class Vehicle(models.Model):
    type = models.ForeignKey(VehicleType, on_delete=models.CASCADE, null=True)
    date_created = models.DateField()
    real_cost = models.FloatField()
    size = models.ForeignKey(VehicleSize, on_delete=models.CASCADE, null=True)


class Rental(models.Model):
    rental_date = models.DateField
    return_date = models.DateField
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, null=True)


class RentalRate(models.Model):
    daily_rate = models.FloatField()
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.CASCADE, null=True)
    vehicle_size = models.ForeignKey(VehicleSize, on_delete=models.CASCADE, null=True)





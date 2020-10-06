from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=26)
    last_name = models.CharField(max_length=26)
    email = models.EmailField(max_length=26)
    phone_number = models.CharField(max_length=26)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=26)
    country = models.CharField(max_length=26)


class VehicleType(models.Model):
    name = models.CharField(max_length=10)


class VehicleSize(models.Model):
    size = models.SmallIntegerField()


class Vehicle(models.Model):
    type = models.ForeignKey(VehicleType, on_delete=models.CASCADE, null=True)
    date_created = models.DateField()
    real_cost = models.DecimalField(decimal_places=2, max_digits=5)
    size = models.ForeignKey(VehicleSize, on_delete=models.CASCADE, null=True)


class Rental(models.Model):
    rental_date = models.DateField
    return_date = models.DateField
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, null=True)


class RentalRate(models.Model):
    daily_rate = models.DecimalField(decimal_places=2, max_digits=5)
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.CASCADE, null=True)
    vehicle_size = models.ForeignKey(VehicleSize, on_delete=models.CASCADE, null=True)





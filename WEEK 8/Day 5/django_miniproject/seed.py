import os
import random

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_miniproject.settings')
django.setup()

# After setup()
from bike_rental.models import *
from faker import Faker
f = Faker()

while Customer.objects.count() < 20:

    first_name = f.first_name()
    last_name = f.last_name()

    customer = Customer.objects.create(
        first_name=first_name,
        last_name=last_name,
        email=f'{first_name}.{last_name}@example.com',
        phone_number=f.numerify('###-###-####'),
        address=f.address(),
        city=f.city(),
        country=f.country()
    )

for size in SIZE_CHOICES:
    VehicleSize.objects.get_or_create(name=size[0])

for item in TYPE_CHOICES:
    VehicleType.objects.get_or_create(name=item[0])

for vtype in VehicleType.objects.all():
    for size in VehicleSize.objects.all():
        rate, created = RentalRate.objects.get_or_create(vehicle_type=vtype, vehicle_size=size)
        if created:
            rate.daily_rate = random.randint(1, 100)
            rate.save()

while Vehicle.objects.count() < 10:

    Vehicle.objects.create(
        size = random.choice(VehicleSize.objects.all()) ,
        date_created=f.date_between(start_date='-1y', end_date='today'),
        real_cost=random.randint(10000, 100000),
        type=random.choice(VehicleType.objects.all())
    )

while Rental.objects.count() < 5:

    Rental.objects.create(
        rental_date=,
        r_
    )
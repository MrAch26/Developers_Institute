import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_miniproject.settings')
django.setup()

# After setup()
from bike_rental.models import models
from faker import Faker

# todo: supprimer ce fichier ou non ?
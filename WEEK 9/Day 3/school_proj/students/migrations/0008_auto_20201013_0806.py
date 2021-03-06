# Generated by Django 3.1.1 on 2020-10-13 08:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('students', '0007_profile_age'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='major',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='minor',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='picture',
        ),
        migrations.RemoveField(
            model_name='student',
            name='profile',
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

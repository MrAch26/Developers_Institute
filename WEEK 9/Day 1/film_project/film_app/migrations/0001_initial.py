# Generated by Django 3.1.2 on 2020-10-12 12:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=15)),
                ('last_name', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=26)),
                ('release_date', models.DateTimeField(auto_now_add=True)),
                ('available_in_countries', models.ManyToManyField(to='film_app.Country')),
                ('category', models.ManyToManyField(to='film_app.Category')),
                ('created_in_country', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='NationalityOfTheFilm', to='film_app.country')),
                ('director', models.ManyToManyField(to='film_app.Director')),
            ],
        ),
    ]
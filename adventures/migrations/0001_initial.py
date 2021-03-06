# Generated by Django 3.1.7 on 2021-03-30 15:08

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdventureLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_name', models.CharField(max_length=100)),
                ('country', django_countries.fields.CountryField(max_length=100)),
            ],
            options={
                'ordering': ['country'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('friendly_name', models.CharField(blank=True, max_length=254, null=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Adventure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('description', models.TextField(max_length=600)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('duration', models.IntegerField(blank=True, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('slot', models.IntegerField(blank=True, null=True)),
                ('rating', models.DecimalField(blank=True, decimal_places=1, max_digits=6, null=True)),
                ('image_url', models.URLField(blank=True, max_length=1024, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='adventure_images')),
                ('adventure_location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='adventures.adventurelocation')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='adventures.category')),
            ],
            options={
                'ordering': ['category'],
            },
        ),
    ]

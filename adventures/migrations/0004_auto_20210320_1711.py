# Generated by Django 3.1.7 on 2021-03-20 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adventures', '0003_auto_20210318_2310'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adventure',
            name='departure_time',
        ),
        migrations.AlterField(
            model_name='adventure',
            name='rating',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='adventure',
            name='return_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
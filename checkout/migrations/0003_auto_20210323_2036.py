# Generated by Django 3.1.7 on 2021-03-23 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_auto_20210321_2226'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderlineitem',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='orderlineitem',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
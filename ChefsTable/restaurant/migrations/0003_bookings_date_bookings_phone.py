# Generated by Django 4.2.13 on 2024-06-08 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_menu_menu_item_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookings',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='bookings',
            name='phone',
            field=models.IntegerField(null=True),
        ),
    ]

# Generated by Django 4.0.4 on 2022-04-13 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0002_hotel_bed_quantity_hotel_price_hotel_region'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='stars',
            field=models.IntegerField(default=0),
        ),
    ]

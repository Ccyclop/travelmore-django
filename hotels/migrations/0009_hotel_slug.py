# Generated by Django 4.0.4 on 2022-04-17 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0008_alter_hotel_hotelname'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
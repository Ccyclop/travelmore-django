from django.db import models
from users.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse

class Hotel(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    slug = models.SlugField(null=True, unique=True)
    hotelName = models.CharField(max_length=255, unique=True)
    thumbnail = models.ImageField(upload_to='hotels/media', blank=True, default='hotels/photos/no-image.png')
    hotelImage = models.ImageField(upload_to='hotels/media', blank=True, default='hotels/photos/no-image.png')
    description = models.TextField()
    stars = models.IntegerField(default=1,validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ])

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.hotelName

    def get_absolute_url(self):
        return reverse("travelmore:hotel-info", kwargs={"slug": self.slug})
    

class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)

    body = models.TextField()
    stars = models.IntegerField(default=1, validators=[
        MaxValueValidator(5),
        MinValueValidator(1)
        ])

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.hotel.hotelName} - {self.user.username}'
    

class Location(models.Model):
    hotel = models.OneToOneField(Hotel, on_delete=models.CASCADE)

    region = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.hotel.hotelName
    
class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)

    choices = (
        (1, ('Normal')),
        (2, ('Vip')),
        (3, ('Deluxe'))
    )

    tp = models.IntegerField(choices=choices, default=1)
    room_image1 = models.ImageField(upload_to='hotels/rooms', blank=True, default='hotels/photos/no-image.png')
    room_image2 = models.ImageField(upload_to='hotels/rooms', blank=True)
    room_image3 = models.ImageField(upload_to='hotels/rooms', blank=True)
    room_image4 = models.ImageField(upload_to='hotels/rooms', blank=True)
    room_mass = models.PositiveIntegerField(default=0)
    floor = models.PositiveIntegerField(default=1)
    beds = models.PositiveIntegerField(default=1)
    bathroom = models.PositiveIntegerField(default=1)
    kitchen = models.PositiveIntegerField(default=0)
    price = models.PositiveIntegerField(default=0)
    balcony = models.BooleanField(default=False)
    fire_extinguisher = models.BooleanField(default=False)
    minibar = models.BooleanField(default=False)
    telephone = models.BooleanField(default=False)
    wifi = models.BooleanField(default=False)
    tv = models.BooleanField(default=False)
    booked = models.BooleanField(default=False)

    def __str__(self):
        return self.hotel.hotelName
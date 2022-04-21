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
    

class feedback(models.Model):
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
    

class location(models.Model):
    hotel = models.OneToOneField(Hotel, on_delete=models.CASCADE)

    region = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.hotel.hotelName
    
class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)

    room_image1 = models.ImageField(upload_to='hotels/rooms', blank=True)
    room_image2 = models.ImageField(upload_to='hotels/rooms', blank=True)
    room_image3 = models.ImageField(upload_to='hotels/rooms', blank=True)
    room_image4 = models.ImageField(upload_to='hotels/rooms', blank=True)
    room_mass = models.IntegerField(default=0, validators=[
        MinValueValidator(0)
    ])
    floor = models.IntegerField(default=1, validators=[
        MinValueValidator(1)
    ])
    beds = models.IntegerField(default=0, validators=[
        MinValueValidator(1)
    ])
    bathroom = models.IntegerField(default=0, validators=[
        MinValueValidator(1)
    ])
    kitchen = models.IntegerField(default=0, validators=[
        MinValueValidator(0)
    ])
    price = models.IntegerField(default=0, validators=[
        MinValueValidator(0)
    ])
    balcony = models.BooleanField(default=False)
    fire_extinguisher = models.BooleanField(default=False)
    minibar = models.BooleanField(default=False)
    telephone = models.BooleanField(default=False)
    wifi = models.BooleanField(default=False)
    tv = models.BooleanField(default=False)

    def __str__(self):
        return self.hotel.hotelName
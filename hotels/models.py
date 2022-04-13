from django.db import models
from users.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Hotel(models.Model):
    hotelName = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    thumbnail = models.ImageField(upload_to='hotels/media', blank=True, default='hotels/photos/no-image.png')
    hotelImge = models.ImageField(upload_to='hotels/media', blank=True, default='hotels/photos/no-image.png')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    describtion = models.TextField()
    bed_quantity = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    stars = models.IntegerField(default=1,validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ])

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.hotelName
from django.db import models
from users.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse

class Hotel(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(null=True, unique=True)
    hotelName = models.CharField(max_length=255, unique=True)
    region = models.CharField(max_length=255)
    thumbnail = models.ImageField(upload_to='hotels/media', blank=True, default='hotels/photos/no-image.png')
    hotelImage = models.ImageField(upload_to='hotels/media', blank=True, default='hotels/photos/no-image.png')
    description = models.TextField()
    price = models.IntegerField(default=0)
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
    


from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    avatar = models.ImageField(upload_to='users/media', blank=True, default='users/avatars/default-user-avatar.png')
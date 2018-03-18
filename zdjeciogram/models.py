from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now


class Photo(models.Model):
    """Model zdjęcia"""
    path = models.ImageField(upload_to='zdjecia/')
    """Pole zdjęciowe."""
    description = models.TextField()
    creation_date = models.DateTimeField(default=now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

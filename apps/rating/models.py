from pyexpat import model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth import get_user_model

from apps.hotels.models import Hotel

User = get_user_model()


class Rating(models.Model):
    author = models.ForeignKey(User, related_name='rating', on_delete=models.SET_NULL, null=True)
    hotel = models.ForeignKey(Hotel, related_name='rating', on_delete=models.CASCADE)
    rating = models.IntegerField(default=1, validators=[MaxValueValidator(10), MinValueValidator(1)])

    def __str__(self):
        return str(self.hotel.title)


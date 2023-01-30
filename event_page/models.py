from django.db import models
from django.contrib.auth import get_user_model

user = get_user_model()

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='events/static')
    description = models.TextField()
    location = models.TextField()
    date_time = models.DateTimeField()
    organiser = models.CharField(max_length=100)
    seats = models.PositiveIntegerField()
    booked_seats = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
        
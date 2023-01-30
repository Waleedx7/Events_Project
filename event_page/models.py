from django.db import models

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='events/static')
    organiser = models.CharField(max_length=100)
    seats = models.PositiveIntegerField()
    booked_seats = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
        
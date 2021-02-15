from django.db import models
from django.urls import reverse
import random

class Event(models.Model):
    title = models.CharField(max_length=250)
    start_date = models.DateField()
    end_date = models.DateField()
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)

    def __str__(self):
        return self.title

def random_string():
    return str(random.randint(100000, 999999))

class ReservationCode(models.Model):
    code = models.CharField(default=random_string, max_length=10)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    reserved = models.BooleanField(default=True)

    def get_absoulte_url(self):
        return reverse('reservation', args=[str(self.code)])
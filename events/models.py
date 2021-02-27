from django.db import models
from django.urls import reverse
import random
import string

class Event(models.Model):
    title = models.CharField(max_length=250)
    start_date = models.DateField()
    end_date = models.DateField()
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)

    def __str__(self):
        return self.title

def random_string():
    alphabet = list(string.ascii_letters)
    str = ''
    for i in range(15):
        idx = random.randint(0,len(alphabet)-1)
        str += alphabet[idx]
    return str


class ReservationCode(models.Model):
    code = models.CharField(default=random_string, max_length=15)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    reserved = models.BooleanField(default=True)
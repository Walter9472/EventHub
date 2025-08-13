from enum import Enum

from django.conf import settings
from django.db import models

# Create your models here.

class EventCategory(Enum):
    CONCERT = 'Concert'
    FESTIVAL = 'Festival'
    SPORT = 'Sport'
    THEATER = 'Theater'
    CONFERENCE = 'Conference'


class Event(models.Model):
    title = models.CharField(max_lenght = 100)
    desc = models.TextField()
    location = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE,
                              related_name='events')
    capacity = models.IntegerField()
    price = models.FloatField()
    category = models.CharField(max_length=50,choices=[(tag.value,tag.value) for tag in EventCategory])
    img = models.ImageField

class TicketStaus(Enum):
    PAID = 'Paid'
    RESERVED = 'Reserved'

class Ticket(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE,related_name='tickets' )
    buyer = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE,
                              related_name='tickets')
    seat = None
    purchase_date = None
    status = models.CharField(max_length=50,choices=[(tag.value,tag.value) for tag in TicketStaus])
    qr_code = None



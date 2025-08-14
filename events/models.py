
from django.conf import settings
from django.db import models

# Create your models here.

class EventCategory(models.TextChoices):
    CONCERT = ('concert','Concert')
    FESTIVAL = ('festival','Festival')
    SPORT = ('sport','Sport')
    THEATER = ('theater','Theater')
    CONFERENCE = ('conference','Conference')


class Event(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE,
                              related_name='events')
    capacity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=8,decimal_places=2)
    category = models.CharField(max_length=50,choices=EventCategory.choices)
    img = models.ImageField(upload_to="event/pics")

    def __str__(self):
        return self.title

class TicketStatus(models.TextChoices):
    PAID = ('paid', 'Paid')
    RESERVED = ('reserved','Reserved')

class Ticket(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE,related_name='tickets' )
    buyer = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE,
                              related_name='tickets')
    seat = models.CharField(max_length=50,blank=True)
    purchase_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50,choices=TicketStatus.choices,default=TicketStatus.RESERVED)
    qr_code = models.CharField(max_length=255,blank=True)

    def __str__(self):
        return f"{self.event.title} – {self.buyer}"




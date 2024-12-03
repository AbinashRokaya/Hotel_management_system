from django.db import models
from django.utils import timezone
from room.models import Room
from guest.models import Guest

# Status=[
#     ('C','Confirmed'),
#     ('P','Pending'),
#     ('X','Cancelled')
# ]

# Create your models here.
class Reservation(models.Model):
    class Status(models.TextChoices):
        PENDING = 'pending', 'Pending'
        CONFIRMED = 'confirmed', 'Confirmed'
        CANCELLED = 'cancelled', 'Cancelled'
    check_in = models.DateField(default=timezone.now)
    check_out = models.DateField(default=timezone.now)
    status = models.CharField(max_length=10,choices=Status.choices,default=None)
    guest_id=models.ForeignKey(Guest,on_delete=models.CASCADE,related_name='guest_id',default=None)
    room_id=models.ForeignKey(Room,on_delete=models.CASCADE,related_name='room_id',default=None)
    


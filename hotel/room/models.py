from django.db import models
from hot.models import Hotel

Type=[
    ('S','Single'),
    ('D','Double'),
    ('S','Suite')
]

# Create your models here.
class Room(models.Model):
    room_no = models.IntegerField()
    type = models.CharField(max_length=10,choices=Type,default=None)
    price = models.DecimalField(max_digits=6,decimal_places=2)
    availability = models.BooleanField()
    capacity = models.IntegerField()
    feature = models.TextField()
    hotel_id=models.ForeignKey(Hotel,on_delete=models.CASCADE,related_name='rooms',default=None)



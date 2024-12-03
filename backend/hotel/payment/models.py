from django.db import models
from django.utils import timezone
from reservation.models import Reservation


Method=[
    ('Credit','Credit'),
    ('Card','Card'),
    ('Cash','Cash'),
    ('Online','Online')
]
Status=[
    ('Completed','Completed'),
    ('Pending','Pending'),
    ('Failed','Failed')
    ]
# Create your models here.
class Payment(models.Model):
    amount=models.DecimalField(max_digits=6,decimal_places=2)
    method=models.CharField(max_length=10,choices=Method)
    status=models.CharField(max_length=10,choices=Status)
    data=models.DateField(default=timezone.now)
    reservation_id=models.ForeignKey(Reservation,on_delete=models.CASCADE,related_name='reservation_id',default=None)


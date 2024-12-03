from django.db import models
from django.contrib.auth.models import User

Gender=[
    ('Male','Male'),
    ('Female','Female'),
    ('Other','Other')
]
# Create your models here.
class Guest(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    cantact_number = models.CharField(max_length=15)
    address = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10,choices=Gender)
    layalty_points = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return self.user.username
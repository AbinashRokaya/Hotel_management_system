from django.db import models
from django.contrib.auth.models import User
from hot.models import Hotel

# Create your models here.
class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    shift = models.CharField(max_length=20)
    hire_date = models.DateField()
    hotel_id=models.ForeignKey(Hotel,on_delete=models.CASCADE,related_name='hot_id',default=None)

    def __str__(self):
        return self.user.username
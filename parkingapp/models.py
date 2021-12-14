from django.db import models
from django.core.validators import RegexValidator

# Driver models
class Driver(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='First_name')
    last_name = models.CharField(max_length=100, verbose_name='Last_name')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated')


# Vehicle models
class Vehicle(models.Model):
    driver_id = models.ForeignKey('Driver', related_name='driver',
                                  on_delete=models.SET_NULL, null=True,
                                  verbose_name='Driver')
    make = models.CharField(max_length=100, verbose_name='Make')
    model = models.CharField(max_length=100, verbose_name='Model')
    plate_number = models.CharField(validators=[RegexValidator("[A-Я]{2}\[0-9]{4}\[A-Я]{2}")],
                                    max_length=10, verbose_name='Plate_number')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated')





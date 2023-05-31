from django.db import models
from django.db.models import Model
from pandas import options

# Create your models here.
# helps to enter database for form
# creating fields for form


class Event(models.Model):

    name = models.CharField(max_length=50)
    passport = models.CharField(max_length=100)
    email = models.CharField(max_length=150)
    phone = models.CharField(max_length=10)
    type = models.CharField(max_length=200)
    date = models. DateTimeField(null=True)
    location = models.CharField(max_length=50, default='SOME STRING')
    description = models.CharField(max_length=300)


# This method returns the string representation of an object of that class.
# Here, the __str__() method is returning the value of the name attribute of the object, which is assumed to be a string.


    def __str__(self):
        return self.name

# Uncomment the following imports before adding the Model code

from django.db import models
from django.contrib import admin
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
class CarMake(models.Model):
    name = models.CharField(null=False, max_length=30, default='Car Make')
    description = models.CharField(max_length=1000)
    createMarkYear = models.IntegerField (max_length=4)
    def __str__(self):
        return "Name: " + self.name + "," + \
               "Description: " + self.description + "," +\
               "Mark Year:" + self.createMarkYear


# <HINT> Create a Car Model model `class CarModel(models.Model):`:
class CarModel(models.Model):
    SEDAN = 'Sedan'
    SUV = 'SUV'
    WAGON = 'Wagon'
    MERCEDES = 'Mercedes'
    COUPE = 'Coupe'
    
    TYPE_CHOICES = [
        (SEDAN, 'Sedan'),
        (SUV, 'SUV'),
        (WAGON, 'Wagon'),
        (MERCEDES, 'Mercedes'),
        (COUPE, 'Coupe'),
    ]

    carMake = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(null=False, max_length=30, default='Car Model')
    dealerId = models.IntegerField()
    type = models.CharField(
        null=False,
        max_length=10,
        choices=TYPE_CHOICES,
        default=SEDAN
    )
    year = models.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(now().year)]
    )

    def __str__(self):
        return "Name: " + self.name + "," + \
               "Type: " + self.type + "," + \
               "Year: " + str(self.year)

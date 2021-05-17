from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Company(models.Model):
    name = models.CharField( max_length=100)
    established = models.DateField()
  

    def __str__(self):
        return self.name

class Feature(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Car(models.Model):
    published_by = models.ForeignKey(User, related_name='published_by', on_delete=models.CASCADE,default = "")
    name = models.CharField( max_length=200)
    features = models.ManyToManyField(Feature, related_name='car_feature')
    company =  models.ForeignKey(Company, related_name='car_company', on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Specification(models.Model):
    PETROL = 0
    DIESEL = 0
    fuelChoice = (
        ('PETROL','Petrol'),
        ('DIESEL', 'Diesel')
    )

    fuelType = models.CharField(choices=fuelChoice,default='PETROL', max_length=50)
    engineCapacity = models.IntegerField()
    transmission = models.CharField( max_length=50)
    wheelbase = models.IntegerField()
    groundClearence = models.IntegerField()
    bootSpace = models.IntegerField()
    car = models.OneToOneField(Car, related_name='car_specs', on_delete=models.CASCADE)    
    def __str__(self):
        return '%s %d cc' %(self.transmission,self.engineCapacity)
    
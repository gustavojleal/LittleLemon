from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=100)
    No_of_guests = models.IntegerField(6)
    Booking_Date = models.DateField()
    def __str__(self):
        return self.name 
      
class Menu(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField(5)
    def __str__(self):
        return f'{self.title} : {self.price}'
    
  
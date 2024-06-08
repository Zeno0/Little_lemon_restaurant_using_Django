from django.db import models

# Create your models here.
class Bookings(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    guest_num = models.IntegerField()
    phone = models.IntegerField(null=True)
    date = models.DateField(null=True)
    comment = models.CharField(max_length=1000)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
    
class Menu(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField(null=False)
    menu_item_desc = models.TextField(max_length=1000, default='')

    def __str__(self):
        return self.name
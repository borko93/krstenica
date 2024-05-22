from django.db import models

# Create your models here.
class list_krsteni(models.Model):
    knjiga = models.CharField(max_length=100)
    strana = models.CharField(max_length=1000)
    broj = models.CharField(max_length=100000)

    eparhija = models.CharField(max_length=100)
    hram = models.CharField(max_length=100)
    mjesto = models.CharField(max_length=30)
    godina = models.CharField(max_length=2)

    datum_rodjenja = models.CharField(max_length=100)
    mjesto_rodjenja = models.CharField(max_length=30)

    def __str__(self):
        return self.hram
    

    

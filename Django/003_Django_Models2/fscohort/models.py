from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=50,blank=True)
    last_name = models.CharField(max_length=30)
    number = models.PositiveSmallIntegerField(blank=True)
    

def __str__(self):
    return f'{self.number} - {self.first_name} - {self.last_name}'
    #! 👆Bu method bana tablo baslıklarında number first_name last_name i göster diyor.
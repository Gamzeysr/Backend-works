from django.db import models

# Create your models here.
#! ben fscohort ile ilgili tablolarımı fscohort altındaki models.py dosyasında olusturucam.Yani burada


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    number = models.IntegerField()
    about = models.TextField(bank=True, null=True)
    register = models.DateTimeField(auto_now_add=True)
    # 👆 instanceımın ilk olusturdgum tarihi yazıyor.
    last_update_data = models.DateTimeField(auto_now=True)
    # 👆studentdan herhangi birsey degistirdgim zaman en sonki degistirdiğim tarihi alıyor.
    is_active = models.BooleanField()

# ? Burada ✨Student✨ ismi yakın zamanda olusturacak oldugum tablom ismine takabul ediyor.

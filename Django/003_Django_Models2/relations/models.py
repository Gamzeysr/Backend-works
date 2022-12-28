
from django.db import models
from django.contrib.auth.models import User
#! 👆 djangonun hali hazırda verdiği user modelini yaptık buraya 

# Create your models here.
class Profile(models.Model):
    bio = models.TextField(blank=True)
    image = models.ImageField(upload_to='profile',blank=True,null=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
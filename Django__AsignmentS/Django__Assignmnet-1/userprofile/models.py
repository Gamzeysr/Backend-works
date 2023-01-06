from django.db import models

# Create your models here.
class Profile(models.Model):
    username = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.BigIntegerField(blank=True)
    bio = models.TextField(max_length=100)
    register_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
      return f'{self.username}'

    class Meta:
        ordering = ["username"]
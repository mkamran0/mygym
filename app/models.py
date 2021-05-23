from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=25)
    mobile = models.CharField(max_length=25)
    age = models.CharField(max_length=10)
    city = models.CharField(max_length=35, default="")
    state = models.CharField(max_length=35, default="")
    country = models.CharField(max_length=35, default="")
    gender = models.CharField(max_length=10, default="")
    category = models.CharField(max_length=25, default="")



    def __str__(self):
        return self.name
        
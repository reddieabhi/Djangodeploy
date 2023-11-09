from django.db import models


class People(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    age = models.IntegerField(default=16)
    gender = models.CharField(max_length=100)
    image = models.ImageField(upload_to='people',null=True)


    
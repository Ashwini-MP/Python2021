from django.db import models

# Create your models here.


class Name(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    user_id = models.IntegerField()


class Contact(models.Model):
    Email = models.CharField(max_length=15)


class Address(models.Model):
    city = models.CharField(max_length=15)


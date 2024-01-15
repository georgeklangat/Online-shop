from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image = models.CharField(max_length=2083)


class Offer(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    discount = models.FloatField()


class Registration(models.Model):
    name = models.CharField(max_length=30)
    admission_no = models.CharField(max_length=10)
    email = models.CharField(max_length=12)
    password = models.CharField(max_length=12)


class Details(models.Model):
    product_type = models.CharField(max_length=10)
    product_nature = models.CharField(max_length=255)
    product_location = models.CharField(max_length=255)

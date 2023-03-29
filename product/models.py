from django.db import models

class Product(models.Model):
    title = models.CharField()
    description = models.CharField()
    price = models.CharField()
    category = models.ForeignKey()

class Category(models.Model):
    name = models.CharField()

class Review(models.Model):
    text = models.TextField()
    product = models.ForeignKey()

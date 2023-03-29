from django.db import models

class Product(models.Model):
    title = models.CharField()
    description = models.CharField()
    price = models.CharField()
    category = models.ForeignKey()

    def __str__(self):
        return self.title
class Category(models.Model):
    name = models.CharField()

    def __str__(self):
        return self.name
class Review(models.Model):
    text = models.TextField()
    product = models.ForeignKey()

    def __str__(self):
        return self.text


from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Pizza(models.Model):
    pizza_name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.pizza_name


class Topping(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    topping_name = models.CharField(max_length=200)

    def __str__(self):
        return self.topping_name

class Comment(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    comment = models.TextField(max_length=200)
    
    def __str__(self):
        return self.comment
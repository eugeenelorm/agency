import email
from email import message
from turtle import position
from django.db import models

# Create your models here.
class Contactform(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phonenumber = models.CharField(max_length=50)
    message = models.TextField()

class Portfolio(models.Model):
    image = models.ImageField(upload_to = 'images/', default='images/portfolio.jpeg')
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)

class Team(models.Model):
    image = models.ImageField(upload_to = 'images/', default='images/portfolio.jpeg')
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
from django.db import models

# Create your models here.
class Person(models.Model):
    description = models.CharField(max_length=128)

    # def __init__(self, name):
    #     self.name = name
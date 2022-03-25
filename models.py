from django.db import models

# Create your models here.

class Fruits(models.Model):
    fruit_name=models.CharField(max_length=120)
    place=models.CharField(max_length=120)
    quantity=models.IntegerField()
    cost=models.IntegerField()

    def __str__(self):
        return self.fruit_name

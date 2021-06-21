from django.db import models


class Order(models.Model):
    pick_up = models.CharField(max_length=150)
    deliver = models.CharField(max_length=150)
    weight = models.IntegerField()
    size = models.IntegerField()
    date = models.DateField()
    name = models.CharField(max_length=150)
    phone = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return self.name

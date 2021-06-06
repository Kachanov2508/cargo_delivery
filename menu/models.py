from django.db import models


class Menu(models.Model):
    title = models.CharField(max_length=150)
    link = models.CharField(max_length=300)

    def __str__(self):
        return self.title

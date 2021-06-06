from django.db import models


class Header(models.Model):
    logo = models.ImageField(upload_to='logo/')
    services = models.TextField(blank=True)
    address = models.TextField(blank=True)

from django.db import models


class Slider(models.Model):
    title = models.CharField(max_length=150)
    text = models.CharField(max_length=300)
    link = models.URLField()
    img = models.ImageField(upload_to='slider/')
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.title

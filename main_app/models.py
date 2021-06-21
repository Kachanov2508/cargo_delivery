from django.db import models


class SocialBlock(models.Model):
    title = models.CharField(max_length=150)
    code = models.TextField(blank=True)

    def __str__(self):
        return self.title

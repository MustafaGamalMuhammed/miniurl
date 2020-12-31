from django.db import models


class ShorteneddURL(models.Model):
    url = models.URLField(unique=True)
    key = models.CharField(max_length=7,  unique=True)

    def __str__(self):
        return self.url

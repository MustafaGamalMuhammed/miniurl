from django.contrib import admin
from url_shortener import models
# Register your models here.

admin.site.register([models.ShorteneddURL])
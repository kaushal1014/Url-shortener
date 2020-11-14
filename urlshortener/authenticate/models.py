from django.db import models
from urlhandel.models import short_urls
# Create your models here.
class User(models.Model):
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    urls= models.ManyToManyField(short_urls,related_name="urls", blank=True)
    def __str__(self):
        return f"{self.username}"
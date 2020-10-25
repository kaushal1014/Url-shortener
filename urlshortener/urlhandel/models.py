from django.db import models
from authenticate.models import User
# Create your models here.
class short_urls(models.Model):
    short_url=models.CharField(max_length=20)
    long_url=models.URLField('Url', unique=True)
    
    def __str__(self):
        return f"{self.short_url} is for {self.long_url}"
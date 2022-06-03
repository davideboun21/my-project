from django.db import models
from datetime import datetime


class Features(models.Model):
    name = models.CharField(max_length=120)
    description = models.CharField(max_length=500)


class Posts(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=1999900)
    created_at = models.DateTimeField(default=datetime.now,blank=True)

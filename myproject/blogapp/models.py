from django.db import models

# Create your models here.
class Access(models.Model):
    ip = models.CharField(max_length=20)
    date = models.DateTimeField()
    url = models.CharField(max_length=50)
    full_url = models.CharField(max_length=100)
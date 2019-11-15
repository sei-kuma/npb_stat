from django.db import models

class Segment(models.Model):
    playerStyle = models.CharField(max_length=10)
    team = models.CharField(max_length=10)
    target = models.CharField(max_length=10)
    data = models.CharField(max_length=10)
    num = models.IntegerField()

# Create your models here.

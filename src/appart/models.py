from django.db import models

# Create your models here.
class DetailsAppart(models.Model):
    design = models.CharField(max_length = 200, blank=True)
    loyer = models.IntegerField()
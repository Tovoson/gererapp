from django.db import models

# Create your models here.
class DetailsAppart(models.Model):
    numapp = models.IntegerField(primary_key=True)
    design = models.CharField(max_length = 100, blank=True)
    loyer = models.IntegerField()
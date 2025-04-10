from django.db import models

# Create your models here.


class CrimeRecord(models.Model):
    zipcode = models.CharField(max_length=10)
    total_crime = models.IntegerField()

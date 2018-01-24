from django.db import models


class TemHem(models.Model):
    """
    A data contains temperature and humidity
    Contains only original data
    """
    data_time = models.DateTimeField(auto_now=True)
    temperature = models.FloatField()
    humidity = models.FloatField()


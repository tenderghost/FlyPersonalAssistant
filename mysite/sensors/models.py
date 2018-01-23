from django.db import models


class TemHem(models.Model):
    """
    A data contains temperature and humidity
    """
    data_time = models.DateTimeField(auto_now=True)
    temperature = models.FloatField()
    humidity = models.FloatField()


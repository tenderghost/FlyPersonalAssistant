from django.db import models

# Create your models here.
class PeriodDef(models.Model):
    """
    Define a Period task.
    """
    PERIOD_TYPES = (
        ('Y', "Year"),
        ('M', "Month"),
        ('W', "Week"),
        ('D', "Day")
    )
    name = models.CharField(max_length = 100)
    period_type = models.CharField(max_length = 1, choices = PERIOD_TYPES)

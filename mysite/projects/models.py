from django.db import models

# Create your models here.
class Project(models.Model):
  """
  A Project should be tracked!
  """
  name = models.CharField(max_length = 100)

  # What this project should do?
  content = models.TextField(null=True, blank=True)

  # When this project signed
  contract_sign_date = models.DateField(null=True, blank=True)

  # Contract value of this project
  contract_value = models.FloatField(null=True, blank=True)

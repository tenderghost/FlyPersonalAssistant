from django.db import models


class Plan(models.Model):
    """
    A model represents a plan
    """
    plan_text = models.CharField(max_length=200)
    start_date = models.DateTimeField('plan to begin')
    end_date = models.DateTimeField('plan to end')
    progress = models.IntegerField()

    # Remark of the plan
    remark = models.CharField(max_length = 500, blank = True)

    def __str__(self):
        return self.plan_text

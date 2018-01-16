from django.db import models
from django.utils import timezone


class Plan(models.Model):
    """
    A model represents a plan
    """

    PLAN_STATUS = (
        ('U', 'Not Start'),
        ('I', 'In Progress'),
        ('F', 'Finished')
    )

    plan_text = models.CharField(max_length=200)
    # What category this plan belongs to
    category = models.CharField(max_length=50, blank=True)
    start_date = models.DateTimeField('plan to begin')
    end_date = models.DateTimeField('plan to end')
    # When this plan has finished?
    finished_at = models.DateTimeField(null=True, blank=True)
    # The progress of the plan
    progress = models.IntegerField(default=0)
    # The status of this plan
    status = models.CharField(max_length = 1, choices = PLAN_STATUS, default = 'U')
    # Remark of the plan
    remark = models.CharField(max_length = 500, blank = True)


    def calc_date_percentage(self):
        """
        Calculate the days passed in the whole date span, in percentage
        """
        date_span = self.end_date - self.start_date
        now = timezone.now()

        if now > self.start_date:
            pctg = (now - self.start_date) * 100 / date_span
            pctg = round(pctg, 2)

            return pctg
        else:
            return 'NOT START YET'


    def __str__(self):
        return self.plan_text


class PlanChange(models.Model):
    """
    Plan change log
    """
    # Which plan this change log belongs to
    plan = models.ForeignKey(Plan, on_delete = models.CASCADE)
    change_reason = models.CharField(max_length = 200)
    change_time = models.DateTimeField(auto_now=True)
    
    class Meta:
        # used for change default table name
        db_table = 'plans_plan_change_log'

    def __str__(self):
        return self.plan.plan_text + " -> " + self.change_reason
from django.db import models

class JobApplication(models.Model):
    job_title = models.CharField(max_length=100)
    recent_degree = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    currently_working = models.BooleanField(default=False)
    current_ctc = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    eligible = models.BooleanField(default=False)

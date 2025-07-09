from django.db import models

# Create your models here.

from django.db import models
from job.models import JobRecord, Candidate


class Feedback(models.Model):
    job = models.ForeignKey(
        JobRecord,
        on_delete=models.CASCADE,
        related_name='feedbacks'
    )
    candidate = models.ForeignKey(
        Candidate,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='feedbacks'
    )
    comment = models.TextField()
    rating = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

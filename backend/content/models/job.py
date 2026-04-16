from django.db import models
from .base import BaseContent


class Job(BaseContent):
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    department = models.CharField(max_length=255, blank=True)
    qualification = models.CharField(max_length=255, blank=True)

    last_date = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True)

    apply_link = models.URLField(blank=True)

    job_type = models.CharField(
        max_length=50,
        choices=[
            ('full_time', 'Full Time'),
            ('part_time', 'Part Time'),
            ('internship', 'Internship'),
        ],
        default='full_time'
    )

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
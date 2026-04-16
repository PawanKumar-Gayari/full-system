from django.db import models
from .base import BaseContent


class Blog(BaseContent):
    author = models.CharField(max_length=255)
    tags = models.JSONField(default=list, blank=True)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title
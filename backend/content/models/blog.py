from django.db import models
from .base import BaseContent


# ===============================
# 🔥 CATEGORY MODEL (simple)
# ===============================
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# ===============================
# 🔥 BLOG MODEL (clean + stable)
# ===============================
class Blog(BaseContent):
    author = models.CharField(max_length=255)

    # 🔥 simple category (no slug yet)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='blogs'
    )

    # 🔥 simple tags (JSON for now)
    tags = models.JSONField(default=list, blank=True)

    # 🔥 content
    content = models.TextField(blank=True)

    # 🔥 media
    thumbnail = models.URLField(blank=True)

    # 🔥 feature
    is_featured = models.BooleanField(default=False)

    published_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title
from django.db import models
from content.models.base import BaseContent


# ===============================
# 🔥 PAGE MODEL (CMS CORE)
# ===============================
class Page(BaseContent):
    # 🔥 dynamic content (frontend engine use करेगा)
    content = models.JSONField(default=dict, blank=True)

    # 🔥 page type (future templates)
    template = models.CharField(max_length=100, blank=True)

    # 🔥 homepage control
    is_homepage = models.BooleanField(default=False)

    # 🔥 publish control
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
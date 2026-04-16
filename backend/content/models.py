from django.db import models
from django.utils.text import slugify


# ===============================
# BASE MODEL (CORE ENGINE)
# ===============================
class BaseContent(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
    ]

    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='draft'
    )

    # dynamic content (frontend/AI)
    schema = models.JSONField(default=dict, blank=True)

    # SEO/meta
    meta = models.JSONField(default=dict, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


# ===============================
# BLOG MODEL
# ===============================
class Blog(BaseContent):
    author = models.CharField(max_length=255)
    tags = models.JSONField(default=list, blank=True)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title


# ===============================
# JOB MODEL (🔥 UI MATCH VERSION)
# ===============================
class Job(BaseContent):
    # basic
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    # 🔥 UI fields (card + detail)
    department = models.CharField(max_length=255, blank=True)
    qualification = models.CharField(max_length=255, blank=True)

    last_date = models.DateField(null=True, blank=True)

    description = models.TextField(blank=True)

    # apply button
    apply_link = models.URLField(blank=True)

    # job type
    job_type = models.CharField(
        max_length=50,
        choices=[
            ('full_time', 'Full Time'),
            ('part_time', 'Part Time'),
            ('internship', 'Internship'),
        ],
        default='full_time'
    )

    # system control
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
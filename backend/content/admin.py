from django.contrib import admin
from .models import Blog, Job


# ===============================
# 🔥 BLOG ADMIN
# ===============================
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'author',
        'status',
        'is_featured',
        'created_at'
    )

    list_filter = (
        'status',
        'is_featured',
        'created_at'
    )

    search_fields = (
        'title',
        'author',
        'tags'
    )

    readonly_fields = ('created_at',)

    prepopulated_fields = {'slug': ('title',)}

    ordering = ('-created_at',)

    list_per_page = 20


# ===============================
# 🔥 JOB ADMIN
# ===============================
@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'company',
        'location',
        'job_type',
        'is_active',
        'created_at'
    )

    list_filter = (
        'job_type',
        'is_active',
        'created_at'
    )

    search_fields = (
        'title',
        'company',
        'location'
    )

    readonly_fields = ('created_at',)

    prepopulated_fields = {'slug': ('title',)}

    ordering = ('-created_at',)

    list_per_page = 20
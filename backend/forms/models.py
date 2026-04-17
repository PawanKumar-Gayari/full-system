from django.db import models


class Form(models.Model):
    name = models.CharField(max_length=255)
    schema = models.JSONField(default=dict)

    def __str__(self):
        return self.name


class FormSubmission(models.Model):
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    data = models.JSONField()

    created_at = models.DateTimeField(auto_now_add=True)
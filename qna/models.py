from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

class Question(models.Model):
    title = models.CharField(max_length=255)
    body = CKEditor5Field('body', blank=True, null=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    meta_description = CKEditor5Field(max_length=1160, blank=True, help_text="Optional: Add a custom meta description for SEO.")
    meta_title = models.CharField(max_length=655)

    def __str__(self):
        return self.title

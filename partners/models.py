from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

class Partner(models.Model):
    CATEGORY_CHOICES = [
        ('hotels', 'Hotels'),
        ('tours', 'Tours'),
        ('airlines', 'Airlines'),
        ('boards', 'Boards'),
    ]

    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='partners/')
    body = CKEditor5Field('body', blank=True, null=True)
    link = models.URLField(help_text="External website link", blank=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='hotels')
    meta_description = CKEditor5Field(max_length=1160, blank=True, help_text="Optional: Add a custom meta description for SEO.")

    def __str__(self):
        return self.title

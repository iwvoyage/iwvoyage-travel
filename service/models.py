from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

class ServicePage(models.Model):
    meta_description = CKEditor5Field(max_length=1160, blank=True, help_text="Optional: Add a custom meta description for SEO.")
    header = models.CharField(max_length=255)
    body = CKEditor5Field('body', blank=True, null=True, default='') 

    subheader_1 = models.CharField(max_length=255, blank=True, null=True)
    body_1 = CKEditor5Field('body1', blank=True, null=True, default='') 

    subheader_2 = models.CharField(max_length=255, blank=True, null=True)
    body_2 = CKEditor5Field('body2', blank=True, null=True, default='') 

    subheader_3 = models.CharField(max_length=255, blank=True, null=True)
    body_3 = CKEditor5Field('body3', blank=True, null=True, default='') 

    subheader_4 = models.CharField(max_length=255, blank=True, null=True)
    body_4 = models.TextField(blank=True, null=True)

    image_1 = models.ImageField(upload_to='service/', blank=True, null=True)
    image_2 = models.ImageField(upload_to='service/', blank=True, null=True)
    image_3 = models.ImageField(upload_to='service/', blank=True, null=True)
    image_4 = models.ImageField(upload_to='service/', blank=True, null=True)
    image_5 = models.ImageField(upload_to='service/', blank=True, null=True)

    def __str__(self):
        return self.header

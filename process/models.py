from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


class Process(models.Model):
    image1 = models.ImageField(upload_to='process_images/')
    image2 = models.ImageField(upload_to='process_images/')
    image3 = models.ImageField(upload_to='process_images/')
    image4 = models.ImageField(upload_to='process_images/')

    header = models.CharField(max_length=255)
    subheader1 = models.CharField(max_length=255)
    subheader2 = models.CharField(max_length=255)
    subheader3 = models.CharField(max_length=255)

    body = CKEditor5Field('body', blank=True, null=True, default='') 

    description1 = CKEditor5Field('description1', blank=True, null=True, default='') 
    description2 = CKEditor5Field('description2', blank=True, null=True, default='') 
    description3 = CKEditor5Field('description3', blank=True, null=True, default='') 

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.header

# about/models.py
from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

class AboutPage(models.Model):
    meta_description = CKEditor5Field(max_length=1160, blank=True, help_text="Optional: Add a custom meta description for SEO.")
    header = models.CharField(max_length=255)
    body = CKEditor5Field('body', blank=True, null=True, default='') 
    subheader_1 = models.CharField(max_length=255, blank=True, null=True)
    image_1 = models.ImageField(upload_to='about/', blank=True, null=True)
    image_2 = models.ImageField(upload_to='about/', blank=True, null=True)
    image_3 = models.ImageField(upload_to='about/', blank=True, null=True)
    image_4 = models.ImageField(upload_to='about/', blank=True, null=True)

    def __str__(self):
        return self.header

class TeamMember(models.Model):
    about_page = models.ForeignKey(AboutPage, on_delete=models.CASCADE, related_name='team_members')
    name = models.CharField(max_length=255)
    bio = CKEditor5Field('bio', blank=True, null=True, default='') 
    photo = models.ImageField(upload_to='team/', blank=True, null=True)

    def __str__(self):
        return self.name

from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django.utils.text import slugify


class Destination(models.Model):
    name = models.CharField(max_length=255, default='Unnamed Destination')
    slug = models.SlugField(unique=True, blank=True)
    header = models.CharField(max_length=255, default='Unnamed Destination')
    body = CKEditor5Field('body', config_name='default')
    subheader= models.CharField(max_length=255, default='Unnamed Destination')
    description = CKEditor5Field('description', blank=True, null=True, default='')  # ✅ Fixed comma
    subheader_one= models.CharField(max_length=255, default='Unnamed Destination')
    description_one = CKEditor5Field('description_one', blank=True, null=True, default='')  # ✅ Fixed comma
    subheader_two= models.CharField(max_length=255, default='Unnamed Destination')
    description_two = CKEditor5Field('description_two', blank=True, null=True, default='')  # ✅ Fixed comma
    subheader_three= models.CharField(max_length=255, default='Unnamed Destination')
    description_three = CKEditor5Field('description_three', blank=True, null=True, default='')  # ✅ Fixed comma
    hero = models.ImageField(upload_to='destinations/', blank=True, null=True, default=None)
    image_banner = models.ImageField(upload_to='destinations/', blank=True, null=True, default=None)
    image2 = models.ImageField(upload_to='destinations/', blank=True, null=True, default=None)
    image3 = models.ImageField(upload_to='destinations/', blank=True, null=True, default=None)
    image4 = models.ImageField(upload_to='destinations/', blank=True, null=True, default=None)
    image5 = models.ImageField(upload_to='destinations/', blank=True, null=True, default=None)
    meta_title = models.CharField(max_length=655)
    meta_description = CKEditor5Field(max_length=1160, blank=True, help_text="Optional: Add a custom meta description for SEO.")
   

    def __str__(self):
        return self.name

    @property
    def hero_url(self):
        if self.hero and hasattr(self.hero, 'url'):
            return self.hero.url
        return '/static/images/default-hero.jpg'  # 👈 or use your own fallback
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)  # Automatically generate "japan" from "Japan"
        super().save(*args, **kwargs)

class Section(models.Model):
    destination = models.ForeignKey(Destination, related_name='sections', on_delete=models.CASCADE)
    subheader = models.CharField(max_length=255, default='Subheader')
    paragraph = CKEditor5Field('Text', config_name='extends')  # ✅ Upgraded to rich text

    def __str__(self):
        return f"{self.destination.name} - {self.subheader}"

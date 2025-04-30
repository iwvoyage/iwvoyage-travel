from django.db import models
from django.utils.text import slugify
from destinations.models import Destination
from django_ckeditor_5.fields import CKEditor5Field

class City(models.Model):
    destination = models.ForeignKey(
        Destination,
        on_delete=models.CASCADE,
        related_name='cities',
        default=1
    )
    name = models.CharField(max_length=255, default='Unnamed Destination')
    slug = models.SlugField(unique=True, default='default-slug')
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
    image = models.ImageField(upload_to='destinations/', blank=True, null=True, default=None)
    image2 = models.ImageField(upload_to='destinations/', blank=True, null=True, default=None)
    image3 = models.ImageField(upload_to='destinations/', blank=True, null=True, default=None)
    image4 = models.ImageField(upload_to='destinations/', blank=True, null=True, default=None)
    image5 = models.ImageField(upload_to='destinations/', blank=True, null=True, default=None)


    def __str__(self):
        return f"{self.name} ({self.destination.header})"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

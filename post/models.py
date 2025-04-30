from django.db import models
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Post(models.Model):
    meta_description = CKEditor5Field(max_length=1160, blank=True, help_text="Optional: Add a custom meta description for SEO.")
    image_hero = models.ImageField(upload_to='posts/sections/', blank=True, null=True)
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    body = CKEditor5Field('body', blank=True, null=True, default='')
    categories = models.ManyToManyField(Category, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Section(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='sections')
    subheader = models.CharField(max_length=255)
    paragraph = CKEditor5Field('paragraph', blank=True, null=True, default='')
    image = models.ImageField(upload_to='posts/sections/', blank=True, null=True)
    image_2 = models.ImageField(upload_to='posts/sections/', blank=True, null=True)  # New image


    def __str__(self):
        return f"{self.subheader} (Post: {self.post.title})"

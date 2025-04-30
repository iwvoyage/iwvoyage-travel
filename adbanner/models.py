from django.db import models

class AdBanner(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='ad_banners/')
    link = models.URLField()

    def __str__(self):
        return self.title

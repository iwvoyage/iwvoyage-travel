from django.db import models

class ImageMedia(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='mediahub/images/')
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title


class VideoMedia(models.Model):
    title = models.CharField(max_length=255)
    video_file = models.FileField(upload_to='mediahub/videos/', blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title


class LinkMedia(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField()

    def __str__(self):
        return self.title

from django.db import models
from django.utils import timezone

class Deal(models.Model):
    title = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='deals/')
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField()
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-start_date']

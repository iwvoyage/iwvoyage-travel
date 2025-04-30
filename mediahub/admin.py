from django.contrib import admin
from .models import ImageMedia, VideoMedia, LinkMedia

admin.site.register(ImageMedia)
admin.site.register(VideoMedia)
admin.site.register(LinkMedia)

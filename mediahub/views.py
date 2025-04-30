from django.shortcuts import render
from .models import ImageMedia, VideoMedia, LinkMedia
from index.models import Trend  # or whatever your model is called
from adbanner.models import AdBanner  # 👈 Import the model

def mediahub_home(request):
    banners = AdBanner.objects.all()
    images = ImageMedia.objects.all()
    videos = VideoMedia.objects.all()
    links = LinkMedia.objects.all()
    trends = Trend.objects.all()[:5]
    return render(request, 'mediahub/mediahub_home.html', {
        'images': images,
        'videos': videos,
        'links': links,
        'trends': trends,
        'banners': banners
    })

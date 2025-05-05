import os

from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from .models import CarouselItem, ItinerarySection, GalleryGrid, Banner, Trend
import uuid
from storages.backends.s3boto3 import S3Boto3Storage

def home(request):
    carousel_items = CarouselItem.objects.all()
    itinerary_section = ItinerarySection.objects.first()
    gallery = GalleryGrid.objects.first()  # ✅ Only get ONE object
    banner = Banner.objects.first()  # Only showing one banner
    trends = Trend.objects.all()

    context = {
        'carousel_items': carousel_items,
        'itinerary_section': itinerary_section,
        'gallery': gallery,
        'banner': banner,
        'trends': trends,
    }

    # 🆕 Add individual itinerary fields
    if itinerary_section:
        context.update({
            'itinerary_1_title': itinerary_section.itinerary_1_title,
            'itinerary_1_destination': itinerary_section.itinerary_1_destination,
            'itinerary_1_link': itinerary_section.itinerary_1_link,
            'itinerary_1_image': itinerary_section.itinerary_1_image,

            'itinerary_2_title': itinerary_section.itinerary_2_title,
            'itinerary_2_destination': itinerary_section.itinerary_2_destination,
            'itinerary_2_link': itinerary_section.itinerary_2_link,
            'itinerary_2_image': itinerary_section.itinerary_2_image,

            'itinerary_3_title': itinerary_section.itinerary_3_title,
            'itinerary_3_destination': itinerary_section.itinerary_3_destination,
            'itinerary_3_link': itinerary_section.itinerary_3_link,
            'itinerary_3_image': itinerary_section.itinerary_3_image,

            'itinerary_4_title': itinerary_section.itinerary_4_title,
            'itinerary_4_destination': itinerary_section.itinerary_4_destination,
            'itinerary_4_link': itinerary_section.itinerary_4_link,
            'itinerary_4_image': itinerary_section.itinerary_4_image,

            'itinerary_5_title': itinerary_section.itinerary_5_title,
            'itinerary_5_destination': itinerary_section.itinerary_5_destination,
            'itinerary_5_link': itinerary_section.itinerary_5_link,
            'itinerary_5_image': itinerary_section.itinerary_5_image,
        })

    return render(request, 'index/home.html', context)


def gallery_view(request):
    gallery = GalleryGrid.objects.first()
    return render(request, 'index/gallery.html', {
        'gallery': gallery
    })




from storages.backends.s3boto3 import S3Boto3Storage

class PublicMediaStorage(S3Boto3Storage):
    location = 'media'
    default_acl = 'public-read'
    file_overwrite = False

def test_s3_upload(request):
    context = {}

    if request.method == 'POST' and request.FILES.get('file'):
        uploaded_file = request.FILES['file']
        file_name = uploaded_file.name
        unique_suffix = uuid.uuid4().hex[:7]
        new_name = f"{os.path.splitext(file_name)[0]}_{unique_suffix}{os.path.splitext(file_name)[1]}"

        storage = PublicMediaStorage()
        saved_path = storage.save(new_name, uploaded_file)
        file_url = storage.url(saved_path)

        print("✅ FILE URL:", file_url)
        context['file_url'] = file_url

    return render(request, 'index/test_upload.html', context)

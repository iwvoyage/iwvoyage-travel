from django.shortcuts import render
from .models import CarouselItem, ItinerarySection, GalleryGrid, Banner, Trend

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

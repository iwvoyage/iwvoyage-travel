from django.contrib import admin
from django.utils.html import format_html
from .models import (
    CarouselItem,
    ItinerarySection,
    GalleryItem,
    GalleryGrid,
    Banner,
    Trend,
)

# Carousel Admin
@admin.register(CarouselItem)
class CarouselItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'title', 'is_active', 'text_alignment', 'image_preview']
    list_editable = ['is_active', 'text_alignment']
    list_filter = ['is_active', 'text_alignment']
    ordering = ['order']

    fieldsets = (
        ('Desktop Version', {
            'fields': ('title', 'subtitle', 'image', 'button_text', 'button_link', 'text_alignment')
        }),
        ('Mobile Version', {
            'fields': ('mobile_title', 'mobile_subtitle', 'mobile_image', 'mobile_button_text', 'mobile_button_link')
        }),
        ('Other Settings', {
            'fields': ('order', 'is_active')
        }),
    )

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height: 50px;">', obj.image.url)
        return "-"
    image_preview.short_description = 'Preview'


# Itinerary Admin
@admin.register(ItinerarySection)
class ItinerarySectionAdmin(admin.ModelAdmin):
    list_display = ('itinerary_1_title', 'itinerary_2_title', 'itinerary_3_title')

    fieldsets = (
        ('Itinerary 1', {
            'fields': ('itinerary_1_title', 'itinerary_1_destination', 'itinerary_1_image', 'itinerary_1_link')
        }),
        ('Itinerary 2', {
            'fields': ('itinerary_2_title', 'itinerary_2_destination', 'itinerary_2_image', 'itinerary_2_link')
        }),
        ('Itinerary 3', {
            'fields': ('itinerary_3_title', 'itinerary_3_destination', 'itinerary_3_image', 'itinerary_3_link')
        }),
        ('Itinerary 4', {
            'fields': ('itinerary_4_title', 'itinerary_4_destination', 'itinerary_4_image', 'itinerary_4_link')
        }),
        ('Itinerary 5', {
            'fields': ('itinerary_5_title', 'itinerary_5_destination', 'itinerary_5_image', 'itinerary_5_link')
        }),
    )


# Gallery Grid Admin (12 cards)
@admin.register(GalleryGrid)
class GalleryGridAdmin(admin.ModelAdmin):
    list_display = ('section_title',)

    def get_fieldsets(self, request, obj=None):
        fieldsets = [
            ("Section Info", {'fields': ('section_title', 'filter_html')}),
        ]
        for i in range(1, 13):
            fieldsets.append((
                f"Card {i}", {
                    'fields': [
                        f'image_{i}', f'title_{i}', f'location_{i}',
                        f'stars_{i}', f'price_{i}', f'page_link_{i}'  # ❌ removed img_link
                    ]
                }
            ))
        return fieldsets


# Banner Admin
@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('header', 'subheader', 'link')


# Trends Admin
@admin.register(Trend)
class TrendAdmin(admin.ModelAdmin):
    list_display = ('title', 'location')

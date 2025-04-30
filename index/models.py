from django.db import models

class CarouselItem(models.Model):
    # Desktop version fields
    title = models.CharField(max_length=255, blank=True, null=True)
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='carousel_images/')
    button_text = models.CharField(max_length=50, blank=True, null=True)
    button_link = models.URLField(blank=True, null=True)

    # Alignment options for desktop
    alignment_choices = [
        ('left', 'Left'),
        ('center', 'Center'),
        ('right', 'Right'),
    ]
    text_alignment = models.CharField(max_length=6, choices=alignment_choices, default='center')

    # Mobile version fields
    mobile_title = models.CharField(max_length=255, blank=True, null=True)
    mobile_subtitle = models.CharField(max_length=255, blank=True, null=True)
    mobile_image = models.ImageField(upload_to='carousel_mobile_images/', blank=True, null=True)
    mobile_button_text = models.CharField(max_length=50, blank=True, null=True)
    mobile_button_link = models.URLField(blank=True, null=True)

    # Active state
    is_active = models.BooleanField(default=False)

    # Order field to control display order
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.order} - {self.title}' if self.title else f'Carousel Item {self.order}'

    class Meta:
        ordering = ['order']  # Order by the 'order' field


        

class ItinerarySection(models.Model):
    # Itinerary 1
    itinerary_1_title = models.CharField(max_length=255)
    itinerary_1_destination= models.CharField(max_length=255)
    itinerary_1_image = models.ImageField(upload_to='itineraries/')
    itinerary_1_link = models.URLField()

    # Itinerary 2
    itinerary_2_title = models.CharField(max_length=255)
    itinerary_2_destination= models.CharField(max_length=255)
    itinerary_2_image = models.ImageField(upload_to='itineraries/')
    itinerary_2_link = models.URLField()

    # Itinerary 3
    itinerary_3_title = models.CharField(max_length=255)
    itinerary_3_destination= models.CharField(max_length=255)
    itinerary_3_image = models.ImageField(upload_to='itineraries/')
    itinerary_3_link = models.URLField()

    # Itinerary 4
    itinerary_4_title = models.CharField(max_length=255)
    itinerary_4_destination= models.CharField(max_length=255)
    itinerary_4_image = models.ImageField(upload_to='itineraries/')
    itinerary_4_link = models.URLField()

    # Itinerary 5
    itinerary_5_title = models.CharField(max_length=255)
    itinerary_5_destination= models.CharField(max_length=255)
    itinerary_5_image = models.ImageField(upload_to='itineraries/')
    itinerary_5_link = models.URLField()

    def __str__(self):
        return "Itinerary Section"



class GalleryItem(models.Model):
    image = models.ImageField(upload_to='gallery/')
    header = models.CharField(max_length=200)
    subheader = models.CharField(max_length=200, blank=True, null=True)
    link = models.URLField()
    grade = models.CharField(max_length=50, help_text='Example: starstarstarstarstar')
    price  = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.header


from django.db import models

class GalleryGrid(models.Model):
    section_title = models.CharField(max_length=255, default="Top 12 Trending for 2025")
    filter_html = models.TextField(help_text="Paste the full <ul> list of filters")

    # Card 1
    image_1 = models.ImageField(upload_to="gallery/")
    title_1 = models.CharField(max_length=255)
    location_1 = models.CharField(max_length=255)
    stars_1 = models.CharField(max_length=100, help_text="e.g. ⭐️⭐️⭐️⭐️⭐️")
    price_1 = models.CharField(max_length=200, blank=True, null=True)
    page_link_1 = models.URLField()

    # Card 2
    image_2 = models.ImageField(upload_to="gallery/", blank=True, null=True)
    title_2 = models.CharField(max_length=255, blank=True, null=True)
    location_2 = models.CharField(max_length=255, blank=True, null=True)
    stars_2 = models.CharField(max_length=100, blank=True, null=True)
    price_2 = models.CharField(max_length=200, blank=True, null=True)
    page_link_2 = models.URLField(blank=True, null=True)

    # Card 3
    image_3 = models.ImageField(upload_to="gallery/", blank=True, null=True)
    title_3 = models.CharField(max_length=255, blank=True, null=True)
    location_3 = models.CharField(max_length=255, blank=True, null=True)
    stars_3 = models.CharField(max_length=100, blank=True, null=True)
    price_3 = models.CharField(max_length=200, blank=True, null=True)
    page_link_3 = models.URLField(blank=True, null=True)

    # Card 4
    image_4 = models.ImageField(upload_to="gallery/", blank=True, null=True)
    title_4 = models.CharField(max_length=255, blank=True, null=True)
    location_4 = models.CharField(max_length=255, blank=True, null=True)
    stars_4 = models.CharField(max_length=100, blank=True, null=True)
    price_4 = models.CharField(max_length=200, blank=True, null=True)
    page_link_4 = models.URLField(blank=True, null=True)

    # Card 5
    image_5 = models.ImageField(upload_to="gallery/", blank=True, null=True)
    title_5 = models.CharField(max_length=255, blank=True, null=True)
    location_5 = models.CharField(max_length=255, blank=True, null=True)
    stars_5 = models.CharField(max_length=100, blank=True, null=True)
    price_5 = models.CharField(max_length=200, blank=True, null=True)
    page_link_5 = models.URLField(blank=True, null=True)

    # Card 6
    image_6 = models.ImageField(upload_to="gallery/", blank=True, null=True)
    title_6 = models.CharField(max_length=255, blank=True, null=True)
    location_6 = models.CharField(max_length=255, blank=True, null=True)
    stars_6 = models.CharField(max_length=100, blank=True, null=True)
    price_6 = models.CharField(max_length=200, blank=True, null=True)
    page_link_6 = models.URLField(blank=True, null=True)

    # Card 7
    image_7 = models.ImageField(upload_to="gallery/", blank=True, null=True)
    title_7 = models.CharField(max_length=255, blank=True, null=True)
    location_7 = models.CharField(max_length=255, blank=True, null=True)
    stars_7 = models.CharField(max_length=100, blank=True, null=True)
    price_7 = models.CharField(max_length=200, blank=True, null=True)
    page_link_7 = models.URLField(blank=True, null=True)

    # Card 8
    image_8 = models.ImageField(upload_to="gallery/", blank=True, null=True)
    title_8 = models.CharField(max_length=255, blank=True, null=True)
    location_8 = models.CharField(max_length=255, blank=True, null=True)
    stars_8 = models.CharField(max_length=100, blank=True, null=True)
    price_8 = models.CharField(max_length=200, blank=True, null=True)
    page_link_8 = models.URLField(blank=True, null=True)

    # Card 9
    image_9 = models.ImageField(upload_to="gallery/", blank=True, null=True)
    title_9 = models.CharField(max_length=255, blank=True, null=True)
    location_9 = models.CharField(max_length=255, blank=True, null=True)
    stars_9 = models.CharField(max_length=100, blank=True, null=True)
    price_9 = models.CharField(max_length=200, blank=True, null=True)
    page_link_9 = models.URLField(blank=True, null=True)

    # Card 10
    image_10 = models.ImageField(upload_to="gallery/", blank=True, null=True)
    title_10 = models.CharField(max_length=255, blank=True, null=True)
    location_10 = models.CharField(max_length=255, blank=True, null=True)
    stars_10 = models.CharField(max_length=100, blank=True, null=True)
    price_10 = models.CharField(max_length=200, blank=True, null=True)
    page_link_10 = models.URLField(blank=True, null=True)

    # Card 11
    image_11 = models.ImageField(upload_to="gallery/", blank=True, null=True)
    title_11 = models.CharField(max_length=255, blank=True, null=True)
    location_11 = models.CharField(max_length=255, blank=True, null=True)
    stars_11 = models.CharField(max_length=100, blank=True, null=True)
    price_11 = models.CharField(max_length=200, blank=True, null=True)
    page_link_11 = models.URLField(blank=True, null=True)

    # Card 12
    image_12 = models.ImageField(upload_to="gallery/", blank=True, null=True)
    title_12 = models.CharField(max_length=255, blank=True, null=True)
    location_12 = models.CharField(max_length=255, blank=True, null=True)
    stars_12 = models.CharField(max_length=100, blank=True, null=True)
    price_12 = models.CharField(max_length=200, blank=True, null=True)
    page_link_12 = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.section_title

    

class Banner(models.Model):
    header = models.CharField(max_length=255)
    subheader = models.CharField(max_length=500, blank=True, null=True)
    banner_image = models.ImageField(upload_to='banners/')
    link = models.URLField(help_text="Link for the CTA button")

    def __str__(self):
        return self.header



class Trend(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    image = models.ImageField(upload_to='trends/')
    link = models.URLField()

    def __str__(self):
        return self.title
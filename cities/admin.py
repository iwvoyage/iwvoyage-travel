from django.contrib import admin
from .models import City

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'slug',
        'destination',
        'get_destination_name',
    )
    search_fields = ('name', 'slug', 'destination__name')
    list_filter = ('destination',)
    prepopulated_fields = {'slug': ('name',)}

    def get_destination_name(self, obj):
        return obj.destination.name
    get_destination_name.short_description = 'Destination Name'

from django.contrib import admin
from .models import Destination, Section

@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']  # ✅ use 'name' instead of 'header'

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ['destination', 'subheader']

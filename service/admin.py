from django.contrib import admin
from .models import ServicePage

@admin.register(ServicePage)
class ServicePageAdmin(admin.ModelAdmin):
    list_display = ('header',)

from django.contrib import admin
from .models import Process

@admin.register(Process)
class ProcessAdmin(admin.ModelAdmin):
    list_display = ('header', 'created_at')
    search_fields = ('header', 'subheader1', 'subheader2', 'subheader3')

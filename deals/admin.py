from django.contrib import admin
from .models import Deal

@admin.register(Deal)
class DealAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title',)

    def save_model(self, request, obj, form, change):
        if obj.is_active:
            # Deactivate all other deals
            Deal.objects.exclude(pk=obj.pk).update(is_active=False)
        super().save_model(request, obj, form, change)

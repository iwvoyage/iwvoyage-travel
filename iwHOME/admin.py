from django.contrib import admin
from django.contrib.admin import AdminSite

class CustomAdminSite(AdminSite):
    site_header = 'iwVoyage Admin Panel'
    site_title = 'iwVoyage Admin'
    index_title = 'Dashboard'

    class Media:
        css = {
            'all': ('admin/css/custom_admin.css',)
        }

# Replace default admin site
admin.site = CustomAdminSite()
admin.autodiscover()

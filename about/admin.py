# about/admin.py
from django.contrib import admin
from .models import AboutPage, TeamMember

class TeamMemberInline(admin.TabularInline):
    model = TeamMember
    extra = 1

@admin.register(AboutPage)
class AboutPageAdmin(admin.ModelAdmin):
    inlines = [TeamMemberInline]
    list_display = ('header',)

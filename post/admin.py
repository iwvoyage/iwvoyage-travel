from django.contrib import admin
from .models import Post, Section, Category, Tag

class SectionInline(admin.StackedInline):
    model = Section
    extra = 1
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" style="max-height: 150px;">'
        return "No Image"
    image_preview.allow_tags = True
    image_preview.short_description = "Image Preview"

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_at')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('categories', 'tags', 'created_at')
    inlines = [SectionInline]
    filter_horizontal = ('categories', 'tags')  # for better UX

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

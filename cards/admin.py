from django.contrib import admin
from .models import Card, Gallery
class GalleryInline(admin.TabularInline):
    fk_name='card'
    model=Gallery

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    inlines = [GalleryInline,]

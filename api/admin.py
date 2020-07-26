from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils.html import format_html
from  api.models import *
from django.conf import settings

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_image')
    def get_image(self, obj):
        return mark_safe(f'<img src={obj.icon.url} width ="100" height="100"')
    get_image.short_description = "icon"

@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')

@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    list_display = ('category', 'level','name', 'get_image')
    def get_image(self, obj):
        return mark_safe(f'<img src={obj.photo.url} width ="100" height="100"')
    get_image.short_description = "photo"

@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    list_display = ('name', 'translation','transcription','example','custom_field')


    def custom_field(self, obj):
        return format_html(f'<link rel="stylesheet" type="text/css" href="{settings.STATIC_URL}scripts/styles.css"><input type="checkbox" id="soundCheck{{1}}" onchange="PlaySound(\'{{0}}\', \'soundCheck{{1}}\', \'{{1}}\', \'un{{1}}\')"></input><label id="un{{1}}" for="soundCheck{{1}}">▶️</label><label class="soundLabel" id="{{1}}" for="soundCheck{{1}}">⏸️</label><script src="{settings.STATIC_URL}scripts/soundmanager2.js"></script><script src="{settings.STATIC_URL}scripts/Player.js"></script>',  obj.sound.url, obj.id)

    custom_field.short_description = "sound"





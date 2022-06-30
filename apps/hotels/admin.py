from django.contrib import admin
from .models import Hotel, HotelImage
from django.contrib import admin
from django.utils.safestring import mark_safe


class InlineHotelImage(admin.TabularInline):
    model = HotelImage
    extra = 1
    fields = ('image',)


class HotelAdmin(admin.ModelAdmin):
    model = Hotel
    list_display = ('title', 'slug', 'city', 'category', 'image', )
    prepopulated_fields = {'slug': ('title', )}
    inlines = [InlineHotelImage, ]
    list_filter = ('category', 'city', )

    def image(self, obj):
        img = obj.image.first()
        if img:
            return mark_safe(f"<img scr='{img.image.url}' width='80' height='80' style='object-fit: contain'/>")
        else:
            return ""


admin.site.register(Hotel, HotelAdmin)
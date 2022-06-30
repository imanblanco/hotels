from django.contrib import admin
from .models import Category


@admin.register(Category)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title', )}
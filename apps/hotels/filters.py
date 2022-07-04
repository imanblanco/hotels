from .models import Hotel
from django_filters.rest_framework import FilterSet


class HotelCategoryFilter(FilterSet):
    class Meta:
        model = Hotel
        fields = ('category',)
from django.urls import path
from .views import HotelListView, CreateHotelView, UpdateHotelView, DestroyHotelView, HotelDetailView

urlpatterns = [
    path('', HotelListView.as_view()),
    path('hotel/', CreateHotelView.as_view()),
    path('hotel/<int:pk>/', HotelDetailView.as_view()),
    path('hotel/update/<int:pk>/', UpdateHotelView.as_view()),
    path('hotel/delete/<int:pk>/', DestroyHotelView.as_view()),

]
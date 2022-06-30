# from django.db import router
# from django.urls import path
# from rest_framework.routers import DefaultRouter
# from .views import FilmViewSet, FilmDetailView

# router = DefaultRouter()

# router.register('', FilmViewSet)

# urlpatterns = [
#     path('<int:pk>/', FilmDetailView.as_view()),

# ]
# urlpatterns += router.urls

from django.urls import path
from .views import HotelListView, CreateHotelView, RetrieveEditDestroyHotelView

urlpatterns = [
    path('', HotelListView.as_view()),
    path('film/', CreateHotelView.as_view()),
    path('film/<int:pk>/', RetrieveEditDestroyHotelView.as_view()),

]
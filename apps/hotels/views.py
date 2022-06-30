# from rest_framework.viewsets import ModelViewSet
# from rest_framework import permissions

# from apps.movie.filters import FilmGenreCountryFilter
# from .models import Film
# from .serializers import FilmSerializer
# from rest_framework import filters, generics


# class FilmViewSet(ModelViewSet):
#     queryset = Film.objects.all()
#     serializer_class = FilmSerializer
#     filterset_class = FilmGenreCountryFilter
#     filter_backends = [filters.SearchFilter]
#     search_fields = ['title']

#     def retrieve(self, request, *args, **kwargs):
#         film = self.get_object()
#         film.views_count += 1
#         film.save()
#         return super(FilmViewSet, self).retrieve(request, *args, **kwargs)

#     def get_permissions(self):
#         if self.action in ['list', 'retrieve']:
#             self.permission_classes = [permissions.AllowAny]
#         elif self.action in ['update', 'create', 'partial_update', 'destroy']:
#             self.permission_classes = [permissions.IsAdminUser]
#         return [permission() for permission in self.permission_classes]

# class FilmDetailView(generics.RetrieveAPIView):
#     queryset = Film.objects.all()
#     serializer_class = FilmSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework import permissions
from rest_framework import generics, filters
from .serializers import HotelSerializer
from .models import Hotel
from rest_framework.pagination import PageNumberPagination


class CreateHotelView(generics.CreateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    serializer_classes = [permissions.IsAdminUser]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class RetrieveEditDestroyHotelView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    permission_classes = [permissions.IsAdminUser]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class HotelListView(generics.ListAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    permission_classes = [permissions.AllowAny]
    pagination_class = PageNumberPagination
    search_fields = ['title']

    def get_serializer_context(self):
        return {'request': self.request}
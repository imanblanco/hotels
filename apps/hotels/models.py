from django.db import models
from apps.category.models import Category
from django.contrib.auth import get_user_model
from slugify import slugify

User = get_user_model()


class Hotel(models.Model):
    admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_pub', verbose_name='Author')
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    content = models.TextField()
    city = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='film_genre', null=True)
    image = models.ImageField(blank=True, null=True, upload_to='Images', default="Images/81KoSSAwH2L._SL1500_.jpg")

    def __str__(self) -> str:
        return f'{self.title} from {self.city}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Hotel, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Отель'
        verbose_name_plural = 'Отели'
        ordering = ['-city']


class HotelImage(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='hotel_images')
    image = models.ImageField(upload_to='hotel_images')

    def __str__(self) -> str:
        return self.hotel
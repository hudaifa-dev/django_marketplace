from django.conf import settings
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.urls import reverse
from django.utils.text import slugify


def download_media_location(instance, filename):
    return f'{instance.slug}, {filename}'


def download_image_location(instance, filename):
    return f'{instance.product.slug}, {filename}'


class Product(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    media = models.FileField(
        blank=True, null=True, upload_to=download_media_location, storage=FileSystemStorage(
            location=settings.PROTECTED_ROOT)
    )
    managers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='managers_product')
    title = models.CharField('Title', max_length=100)
    slug = models.SlugField('Slug', blank=True, null=True, unique=True)
    description = models.TextField('Description', max_length=3000, blank=True, null=True)
    price = models.DecimalField('Price', max_digits=100, decimal_places=2, default=0.00)
    sale_price = models.DecimalField(
        'Sale Price', max_digits=100, decimal_places=2, default=0.00, null=True, blank=True
    )

    def __str__(self):
        return self.title

    @staticmethod
    def get_absolute_url():
        return reverse('products:product_list')

    def get_details_url(self):
        return reverse('products:product_detail', kwargs={'pk': self.pk})

    def get_download(self):
        view_namae = 'products:product_download'
        url = reverse(view_namae, kwargs={'slug': self.slug})
        return url


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null=True, upload_to=download_image_location)

    def __str__(self):
        return f'{self.image}'


class MyProduct(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product, blank=True)

    def __str__(self):
        return f'{self.product.count()}'


# Signals for product
def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Product.objects.filter(slug=slug)
    exists = qs.exists()
    if exists:
        new_slug = '%s-%s' % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


@receiver(pre_save, sender=Product)
def product_pre_save_receiver(instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

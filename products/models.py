from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify


class Product(models.Model):
    title = models.CharField('Title', max_length=100)
    slug = models.SlugField('Slug', blank=True, null=True)
    description = models.TextField('Description', max_length=3000, blank=True, null=True)
    price = models.DecimalField('Price', max_digits=100, decimal_places=2, default=0.00)
    sale_price = models.DecimalField(
        'Sale Price', max_digits=100, decimal_places=2, default=0.00, null=True, blank=True
    )

    def __unicode__(self):
        return self.title


def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if instance.title:
        instance.slug = slugify(instance.title)


pre_save.connect(product_pre_save_receiver, sender=Product)

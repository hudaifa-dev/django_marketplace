from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.urls import reverse
from django.utils.text import slugify


class TagModel(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)
    product = models.ManyToManyField('products.Product', blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("tags:detail", kwargs={"slug": self.slug})


@receiver(pre_save, sender=TagModel)
def tags_pre_save_receiver(instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance)

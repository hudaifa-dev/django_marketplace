# from django.db.models.signals import pre_save
# from django.utils.text import slugify
#
# from products.models import Product
#
#
# def product_pre_save_receiver(sender, instance, *args, **kwargs):
#     if not instance.slug:
#         instance.slug = slugify(instance.title)
#
#
# pre_save.connect(product_pre_save_receiver, sender=Product)

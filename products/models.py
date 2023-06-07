from django.db import models


class Product(models.Model):
    title = models.CharField('Title', max_length=100)
    description = models.TextField('Description', max_length=3000, blank=True, null=True)
    price = models.DecimalField('Price', max_digits=100, decimal_places=2, default=0.00)
    sale_price = models.DecimalField(
        'Sale Price', max_digits=100, decimal_places=2, default=0.00, null=True, blank=True
    )

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

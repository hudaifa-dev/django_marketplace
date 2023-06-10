from django.contrib import admin
from products.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['__unicode__', 'slug', 'id', 'price', 'sale_price']
    list_filter = ['price']
    list_editable = ['sale_price']
    search_fields = ['title', 'description']

    class Meta:
        model = Product


admin.site.register(Product, ProductAdmin)

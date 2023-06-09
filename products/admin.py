from django.contrib import admin
from products.models import Product, MyProduct, ProductImage


class ProductImageAdmin(admin.TabularInline):
    model = ProductImage


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageAdmin]
    list_display = ['slug', 'id', 'price', 'sale_price']
    list_filter = ['price']
    list_editable = ['sale_price']
    search_fields = ['title', 'description']

    class Meta:
        model = Product


admin.site.register(Product, ProductAdmin)
admin.site.register(MyProduct)
admin.site.register(ProductImage)

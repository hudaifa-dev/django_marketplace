from django.contrib import admin
from products.models import Product, MyProduct


class ProductAdmin(admin.ModelAdmin):
    list_display = ['__unicode__', 'slug', 'id', 'price', 'sale_price']
    list_filter = ['price']
    list_editable = ['sale_price']
    search_fields = ['title', 'description']

    class Meta:
        model = Product


class MyProductAdmin(admin.ModelAdmin):
    list_display = ['__unicode__']

    class Meta:
        model = MyProduct


admin.site.register(Product, ProductAdmin)
admin.site.register(MyProduct, MyProductAdmin)

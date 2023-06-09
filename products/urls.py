from django.urls import path
from products.views import list_view, detail_slug_view, create_view

app_name = 'products'
urlpatterns = [
    path('list/', list_view, name='product_list'),
    path('create/', create_view, name='product_create'),
    path('detail/<str:slug>/', detail_slug_view, name='product_detail_slug'),
]

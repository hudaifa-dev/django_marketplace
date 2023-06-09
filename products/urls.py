from django.urls import path
from products.views import list_view, detail_view, detail_slug_view

app_name = 'products'
urlpatterns = [
    path('list/', list_view, name='product_list'),
    path('details/<int:object_id>/', detail_view, name='product_detail'),
    path('detail/<str:slug>/', detail_slug_view, name='product_detail_slug'),
]

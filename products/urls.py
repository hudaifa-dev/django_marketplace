from django.urls import path
from products.views import (
    ProductListView,
    ProductDetailsView,
    ProductCreateView,
    ProductUpdateView,
    ProductDownloadView,
)

app_name = 'products'
urlpatterns = [
    path('list/', ProductListView.as_view(), name='product_list'),
    # ID or Slug
    path('create/', ProductCreateView.as_view(), name='product_create'),
    # path('<str:slug>/', ProductCreateView.as_view(), name='product_create'),
    path('<int:pk>/detail/', ProductDetailsView.as_view(), name='product_detail'),
    path('<str:slug>/detail/', ProductDetailsView.as_view(), name='product_detail'),
    path('<int:pk>/download/', ProductDownloadView.as_view(), name='product_download'),
    path('<str:slug>/download/', ProductDownloadView.as_view(), name='product_download'),

    path('<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
]

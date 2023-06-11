from django.urls import path
from products.views import ProductListView, ProductDetailsView, ProductCreateView, ProductUpdateView

app_name = 'products'
urlpatterns = [
    path('list/', ProductListView.as_view(), name='product_list'),
    # ID or Slug
    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('<str:slug>/', ProductCreateView.as_view(), name='product_create'),
    path('<int:pk>/', ProductDetailsView.as_view(), name='product_detail'),
    path('<str:slug>/', ProductDetailsView.as_view(), name='product_detail'),

    path('<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
]

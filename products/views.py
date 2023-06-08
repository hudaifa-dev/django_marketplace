from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views import generic

from products.models import Product


def list_view(request):
    context = {}
    return render(request, 'templates/product/list.html', context=context)


def detail_slug_view(request, slug=None):
    try:
        product = get_object_or_404(Product, slug=slug)
    except Product.MultipleObjectsReturned:
        product = Product.objects.filter(slug=slug).order_by('-title').first()
    context = {'object': product}
    return render(request, 'templates/product/detail.html', context=context)


def detail_view(request, object_id=None):
    product = get_object_or_404(Product, id=object_id)
    context = {'object': product}
    return render(request, 'templates/product/detail.html', context=context)


class ProductListView(generic.ListView):
    pass


class ProductDetailsView(generic.DetailView):
    pass

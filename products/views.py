from django.views import generic
from products.forms import CreateProductForm
from products.models import Product
from products.mixins import MultipleMixin, SubmitButtonMixin, LoginRequiredMixin, ProductManagerMixin


class ProductListView(generic.ListView):
    model = Product

    def get_queryset(self, *args, **kwargs):
        qs = super(ProductListView, self).get_queryset()
        return qs


class ProductCreateView(LoginRequiredMixin, SubmitButtonMixin, MultipleMixin, generic.CreateView):
    model = Product
    form_class = CreateProductForm
    success_url = '/products/'
    submit_btn = 'Create Product'

    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        valid_data = super(ProductCreateView, self).form_valid(form)
        form.instance.managers.add(user)
        return valid_data


class ProductUpdateView(ProductManagerMixin, SubmitButtonMixin, MultipleMixin, generic.UpdateView):
    model = Product
    form_class = CreateProductForm
    success_url = '/products/'
    submit_btn = 'Update Product'


class ProductDetailsView(MultipleMixin, generic.DetailView):
    model = Product

# def list_view(request):
#     context = {}
#     return render(request, 'templates/products/product_list.html', context=context)


# def detail_slug_view(request, slug=None):
#     try:
#         product = get_object_or_404(Product, slug=slug)
#     except Product.MultipleObjectsReturned:
#         product = Product.objects.filter(slug=slug).order_by('-title').first()
#     context = {'object': product}
#     return render(request, 'templates/products/product_detail.html', context=context)


# def create_view(request):
#     form = CreateProductForm(request.POST or None)
#     if form.is_valid():
#         instance = form.save(commit=False)
#         instance.sale_price = instance.price
#         instance.save()
#     context = {'form': form}
#     return render(request, 'templates/products/product_form.html', context=context)


# def update_view(request, object_id=None):
#     product = get_object_or_404(Product, id=object_id)
#     form = CreateProductForm(request.POST or None, instance=product)
#     if form.is_valid():
#         instance = form.save(commit=False)
#         instance.save()
#     context = {'object': product, 'form': form}
#     return render(request, 'templates/products/update.html', context=context)


# def detail_view(request, object_id=None):
#     products = get_object_or_404(Product, id=object_id)
#     context = {'object': products}
#     return render(request, 'templates/products/product_detail.html', context=context)

import os
from mimetypes import guess_type
from wsgiref.util import FileWrapper

from django.conf import settings
from django.db.models import Q
from django.http import HttpResponse, Http404
from django.views import generic

from products.forms import CreateProductForm
from products.mixins import MultipleMixin, SubmitButtonMixin, LoginRequiredMixin, ProductManagerMixin
from products.models import Product
from tags.models import TagModel


class ProductListView(generic.ListView):
    model = Product

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Product.objects.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query)
            )
        else:
            return Product.objects.all()


class ProductCreateView(LoginRequiredMixin, SubmitButtonMixin, MultipleMixin, generic.CreateView):
    model = Product
    form_class = CreateProductForm
    # success_url = '/products/product_list/'
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
    # success_url = '/products/product_list'
    submit_btn = 'Update Product'

    def get_initial(self):
        initial = super(ProductUpdateView, self).get_initial()
        tags = self.get_object().tagmodel_set.all()
        initial['tags'] = ''.join([x.name for x in tags])
        return initial

    def form_valid(self, form):
        valid_data = super(ProductUpdateView, self).form_valid(form)
        tags = form.cleaned_data.get('tags')
        if tags:
            tag_list = tags.split(',')
            for tag in tag_list:
                new_tag = TagModel.objects.get_or_create(name=str(tag).strip())[0]
                new_tag.product.add(self.get_object())
        return valid_data


class ProductDetailsView(MultipleMixin, generic.DetailView):
    model = Product


class ProductDownloadView(MultipleMixin, generic.DetailView):
    model = Product

    def get(self, request, *args, **kwargs):
        _object = self.get_object()
        if _object in request.user.myproduct.product.all():
            filepath = os.path.join(settings.PROTECTED_ROOT, _object.media.path)
            guessed_type = guess_type(filepath)[0]
            with open(filepath, 'rb') as f:
                wrapper = FileWrapper(f)
                # wrapper = FileWrapper(open(filepath))
                mimetypes = 'application/force-download'
                if guessed_type:
                    mimetypes = guessed_type
                response = HttpResponse(wrapper, content_type=mimetypes)
                if not request.GET.get('preview'):
                    response['Content-Disposition'] = 'attachment; filename="%s"' % _object.media.name
                response['X-SendFile'] = str(_object.media.name)
                return response
        else:
            raise Http404

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

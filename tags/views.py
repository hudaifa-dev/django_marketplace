from django.views import generic

from products.models import Product
from tags.models import TagModel


class TagListView(generic.ListView):
    model = TagModel

    def get_queryset(self):
        return TagModel.objects.all()


class TagDetailView(generic.DetailView):
    model = TagModel

    def get_context_data(self, **kwargs):
        context = super(TagDetailView, self).get_context_data(**kwargs)
        # context['tag_product'] = Product.objects.all()
        return context

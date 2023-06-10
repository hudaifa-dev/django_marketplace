from django.shortcuts import get_object_or_404


class MultipleMixin(object):
    model = None

    def __init__(self):
        self.kwargs = None

    def get_object(self, *args, **kwargs):
        slug = self.kwargs.get('slug')
        ModelClass = self.model
        if slug is not None:
            try:
                product_obj = get_object_or_404(ModelClass, slug=slug)
            except ModelClass.MultipleObjectsReturned:
                product_obj = ModelClass.objects.filter(slug=slug).order_by('-title').first()
        else:
            product_obj = super(MultipleMixin, self).get_object()
        return product_obj


class SubmitButtonMixin(object):
    submit_btn = None

    def get_context_data(self, **kwargs):
        context = super(SubmitButtonMixin, self).get_context_data(**kwargs)
        context['submit_btn'] = self.submit_btn
        return context

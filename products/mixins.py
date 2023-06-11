from django.http import Http404
from django.shortcuts import get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class LoginRequiredMixin(object):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)


class StaffRequiredMixin(object):
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)


class ProductManagerMixin(LoginRequiredMixin, object):
    def __init__(self):
        self.request = None

    def get_object(self, *args, **kwargs):
        user = self.request.user
        obj = super(ProductManagerMixin, self).get_object(*args, **kwargs)
        try:
            obj.user == user
        except:
            raise Http404
        try:
            user in obj.managers.all()
        except:
            raise Http404
        if obj == user or user in obj.managers.all():
            return obj
        else:
            raise Http404


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

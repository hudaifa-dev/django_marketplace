from django import forms
from django.utils.functional import empty

from products.models import Product


class CreateProductForm(forms.ModelForm):
    PUBLISH_CHOICES = (('publish', 'Publish'), ('draft', 'Draft'),)
    publish = forms.ChoiceField(widget=forms.RadioSelect, choices=PUBLISH_CHOICES)

    class Meta:
        model = Product
        fields = ('title', 'description', 'price', 'publish',)

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price <= 1.00:
            raise forms.ValidationError('Price must be greater than $1.00')
        elif price >= 99.99:
            raise forms.ValidationError('Price must be less than $100.00')
        else:
            return price

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) > 3:
            return title
        else:
            raise forms.ValidationError('Title must be greater than 3 characters.')

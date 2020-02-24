from django import forms

from products.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price',
        ]


class RawProductForm(forms.Form):
    title = forms.CharField(label='NO_LABEL')
    description = forms.CharField(required=False, widget=forms.Textarea(
        attrs={
            'class': "new-class",
            'rows': 5,
            'cols': 50,
        }
    ))
    price = forms.DecimalField(initial=199.99)

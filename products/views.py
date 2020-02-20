from django.shortcuts import render

# Create your views here.
from products.models import Product


def product_detail_view(request):
    product = Product.objects.get(id=1)
    context = {
        'obj': product
    }
    return render(request, "products/detail.html", context)

from django.shortcuts import render

# Create your views here.
from products.forms import ProductForm
from products.models import Product


def product_detail_view(request):
    product = Product.objects.get(id=1)
    context = {
        'obj': product
    }
    return render(request, "products/detail.html", context)


def product_create_view(request):
    form = ProductForm(request.POST or None)

    if form.is_valid():
        form.save()
        form = ProductForm()

    context = {'form': form}

    return render(request, "products/create.html", context)

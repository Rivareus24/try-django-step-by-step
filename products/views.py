from django.shortcuts import render

# Create your views here.
from products.forms import ProductForm, RawProductForm
from products.models import Product


def product_detail_view(request):
    product = Product.objects.get(id=1)
    context = {
        'obj': product
    }
    return render(request, "products/detail.html", context)


def product_create_view(request):
    form = RawProductForm(request.GET)
    if request.method == 'POST':
        form = RawProductForm(request.POST or None)
        if form.is_valid():
            print(form.cleaned_data)
            Product.objects.create(**form.cleaned_data)
        else:
            print(form.errors)

    context = {'form': form}

    return render(request, "products/create.html", context)


'''
def product_create_view(request):
    form = ProductForm(request.POST or None)

    if form.is_valid():
        form.save()
        form = ProductForm()

    context = {'form': form}

    return render(request, "products/create.html", context)
'''

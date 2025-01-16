from django.shortcuts import render, HttpResponse
from catalog.models import Category, Product


def get_home(request):
    products = Product.objects.all()
    context = {
        'products': products
    }

    return render(request, 'catalog/home.html', context)


def contacts(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(message)
        return HttpResponse(f'{name}, с номером {phone}, ваше сообщение получено!')
    return render(request, 'catalog/contacts.html')


def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {
        'product': product
    }

    return render(request, 'catalog/product_detail.html', context)

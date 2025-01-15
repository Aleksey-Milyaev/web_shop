from django.shortcuts import render, HttpResponse
from catalog.models import Category, Product


def get_home(request):
    return render(request, 'catalog/home.html')


def contacts(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(message)
        return HttpResponse(f'{name}, с номером {phone}, ваше сообщение получено!')
    return render(request, 'catalog/contacts.html')

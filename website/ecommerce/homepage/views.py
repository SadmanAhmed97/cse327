from django.shortcuts import render


def store(request):
    context = {}
    return render(request, 'homepage/index.html', context)


def cart(request):
    context = {}
    return render(request, 'homepage/cart.html', context)


def checkout(request):
    context = {}
    return render(request, 'homepage/checkout.html', context)

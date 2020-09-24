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


def signup(request):
    context = {}
    return render(request, 'homepage/signup.html', context)


def login(request):
    context = {}
    return render(request, 'homepage/login.html', context)

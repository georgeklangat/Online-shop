from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


def index(request):
    products = Product.objects.all()
    return render(request, 'index.html',
                  {'products':products})


# def offer(request):
#     offer = offer.objects.all()
#     return render(request,)

def personal(request):
    return render(request, 'personal.html')


def coding(request):
    return HttpResponse("This is my coding skill that i always like it")


def best(request):
    return HttpResponse("Welcome to my best products")

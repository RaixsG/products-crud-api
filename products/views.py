from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
from .models import Products

def product_list(request):
  products = Products.objects.all()
  return JsonResponse([{'name': product.name} for product in products], safe=False)
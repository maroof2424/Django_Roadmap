from django.shortcuts import render,redirect,get_object_or_404
from .models import Product
# Create your views here.

def product_list(request):
    products = Product.objects.all().order_by("-created_at")
    return render(request,"store/product_list.html",{"products":products})

def product_details(request,pk):
    product = get_object_or_404(Product,id=pk)
    return render(request,"store/product_detail.html",{"product":product})

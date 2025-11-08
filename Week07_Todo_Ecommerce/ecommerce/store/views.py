from django.shortcuts import render, get_object_or_404
from .models import Product

def product_list(request):
    search = request.GET.get("search", "")
    min_price = request.GET.get("min", "")
    max_price = request.GET.get("max", "")

    products = Product.objects.all()

    # 
    if search:
        products = products.filter(title__icontains=search)

    if min_price:
        products = products.filter(price__gte=min_price)

    if max_price:
        products = products.filter(price__lte=max_price)

    return render(request, "store/product_list.html", {
        "products": products,
        "search": search,
        "min_price": min_price,
        "max_price": max_price,
    })


def product_details(request, pk):
    product = get_object_or_404(Product, id=pk)
    return render(request, "store/product_detail.html", {"product": product})

from django.shortcuts import redirect, get_object_or_404
from .models import Product

def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)

    cart = request.session.get("cart", {})

    if str(pk) in cart:
        cart[str(pk)]["quantity"] += 1
    else:
        cart[str(pk)] = {"quantity": 1}

    request.session["cart"] = cart

    return redirect("cart_page")

def remove_from_cart(request, pk):
    cart = request.session.get("cart", {})

    if str(pk) in cart:
        del cart[str(pk)]

    request.session["cart"] = cart
    return redirect("cart_page")

def cart_page(request):
    cart = request.session.get("cart", {})

    items = []
    total = 0

    for pk, data in cart.items():
        product = Product.objects.get(pk=pk)
        quantity = data["quantity"]
        amount = product.price * quantity

        items.append({
            "product": product,
            "quantity": quantity,
            "amount": amount,
        })

        total += amount

    return render(request, "store/cart.html", {
        "items": items,
        "total": total
    })

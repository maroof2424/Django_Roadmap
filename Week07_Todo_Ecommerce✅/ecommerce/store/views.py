from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Product, Order
from .forms import OrderForm

def product_list(request):
    search = request.GET.get("search", "")
    min_price = request.GET.get("min", "")
    max_price = request.GET.get("max", "")

    products = Product.objects.all()

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
    product = get_object_or_404(Product, pk=pk)
    return render(request, "store/product_detail.html", {"product": product})

def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    cart = request.session.get("cart", {})

    if str(pk) in cart:
        cart[str(pk)]["quantity"] += 1
        messages.info(request, f"Quantity updated for {product.title}")
    else:
        cart[str(pk)] = {"quantity": 1}
        messages.success(request, f"{product.title} added to cart!")

    request.session["cart"] = cart
    return redirect("cart_page")

def remove_from_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    cart = request.session.get("cart", {})

    if str(pk) in cart:
        del cart[str(pk)]
        messages.warning(request, f"{product.title} removed from cart.")

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

        items.append({"product": product, "quantity": quantity, "amount": amount})
        total += amount

    return render(request, "store/cart.html", {
        "items": items,
        "total": total
    })

def checkout(request):
    cart = request.session.get("cart", {})
    if not cart:
        messages.error(request, "Your cart is empty!")
        return redirect("product_list")  
    
    items = []
    total = 0

    for pk, data in cart.items():
        product = Product.objects.get(pk=pk)
        quantity = data["quantity"]
        amount = product.price * quantity

        items.append({"product": product, "quantity": quantity, "amount": amount})
        total += amount

    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.total_price = total
            order.save()

            request.session["cart"] = {}
            messages.success(request, f"Order #{order.id} placed successfully!")

            return render(request, "store/order_success.html", {"order": order})
    else:
        form = OrderForm()

    return render(request, "store/checkout.html", {
        "form": form,
        "items": items,
        "total": total
    })

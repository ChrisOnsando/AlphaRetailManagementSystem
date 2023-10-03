from django.shortcuts import render, get_object_or_404, redirect
from shop.models import Product
from accounts.models import Order
from .forms import ProductForm
from django.urls import reverse_lazy


def product_list(request):
    products = Product.objects.filter(available=True)
    return render(request, 'product/product_list.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'product/product_detail.html', {'product': product})

def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
            
    else:
        form = ProductForm()
    return render(request, 'product/create_product.html', {'form': form})
success_url = reverse_lazy("index")


def place_order(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        quantity = int(request.POST['quantity'])
        if product.available and quantity > 0:
            Order.objects.create(user=request.user, product=product, quantity=quantity)
            return redirect('product_list')
    return render(request, 'product/place_order.html', {'product': product})

def order_list(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'order/order_list.html', {'orders': orders})

def order_detail(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    return render(request, 'order/order_detail.html', {'order': order})
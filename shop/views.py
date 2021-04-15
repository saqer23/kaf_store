from django.shortcuts import render,get_object_or_404
from .models import Product,About
from cart.forms import CartAddProductForm


def product_list(request):
    products = Product.objects.filter(available=True)
    about =About.objects.all()

    context = {
        'products':products,
        'about':about,
    }
    return render(request,'shop/index.html',context)

def product_detail(request,id,slug):
    product = get_object_or_404(Product,id=id , slug=slug,available=True)
    cart_product_form = CartAddProductForm()
    context = {
        'product':product,
        'cart_product_form':cart_product_form,
    }
    return render(request,'shop/details.html',context)
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

from .basket import Basket
from store.models import Product

def basket_summary(request):
    basket = Basket(request)
    return render(request, 'basket/basket.html')


def basket_add(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        product = get_object_or_404(Product, id=product_id)
        basket.add(product=product, qty=product_qty)
        basketqty = basket.__len__()
        response = JsonResponse({'qty': basketqty})
        return response

def basket_delete(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        basket.delete(product=product_id)
        basketqty = basket.__len__()
        baskettotal = basket.get_total_price()
        subtotal = basket.get_subtotal_price()
        response = JsonResponse({'qty': basketqty, 'total': baskettotal, 'subtotal': subtotal,})
        return response

def basket_update(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        basket.update(product=product_id, qty=product_qty)
        basketqty = basket.__len__()
        baskettotal = basket.get_total_price()
        subtotal = basket.get_subtotal_price()
        basket_item_total = basket.get_total_item(product_id)
        response = JsonResponse({'qty': basketqty, 'total': baskettotal, 'subtotal': subtotal, 'itemtotal': basket_item_total})
        return response 
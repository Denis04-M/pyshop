from django.shortcuts import render
from django.http import JsonResponse
import json
import datetime
import random
from django.views.decorators.csrf import csrf_exempt
from .models import *


def index(request):
    products = Product.objects.filter(price=70)
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cat_items']
    return render(request, 'index.html',
                  {'products': products, 'order': order, 'items': items, 'cartItems': cartItems})


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order.get_cart_items
    return render(request, 'cart.html', {'items': items, 'order': order, 'cartItems': cartItems})


def shipping(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
    return render(request, 'shipping.html', {'order': order, 'items': items, 'cartItems': cartItems})


def beverages(request):
    products = Product.objects.filter(category='beverages')
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
    return render(request, 'beverages.html',
                  {'products': products, 'order': order, 'items': items, 'cartItems': cartItems})


def vegetables(request):
    products = Product.objects.filter(category='vegetables')
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
    return render(request, 'vegetables.html',
                  {'products': products, 'order': order, 'items': items, 'cartItems': cartItems})


def meat(request):
    products = Product.objects.filter(category='meat')
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
    return render(request, 'vegetables.html',
                  {'products': products, 'order': order, 'items': items, 'cartItems': cartItems})


def meals(request):
    products = Product.objects.filter(category='main')
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
    return render(request, 'meals.html', {'products': products, 'order': order, 'items': items, 'cartItems': cartItems})


def report(request):
    month = 1
    if request.method == 'POST':
        form = request.POST
        data = dict(form)
        dic = data
        month = dic['dropdown'][0]
        print(month)
    products = Report.objects.filter(month=month).order_by('items_sold')
    # name = 'Githeri'
    # items_sold = 0
    # for mon in range(1, 13):
    #     Report.name = name
    #     month = mon
    #     Report.month = month
    #     items_sold = random.randrange(300, 475)
    #     Report.items_sold = items_sold
    #     Report.save()
    return render(request, 'report.html', {'products': products})


def chart(request):
    products = Chart.objects.all()
    context = {
        'products': products
    }

    return render(request, 'chart.html', context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('ProductId:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)


def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    total = order.get_cart_total
    order.transaction_id = str(transaction_id)

    if int(total) == int(order.get_cart_total):
        order.complete = True
    order.save()
    Shipping.objects.create(
        order=order,
        address=data['shipping']['address'],
        house_number=data['shipping']['house'],
        building=data['shipping']['building'],

    )
    print('Data:', request.body)
    return JsonResponse('Payment complete', safe=False)


@csrf_exempt
def placeOrder(request):
    date = datetime.datetime.now().time()
    transaction_id = date
    data = json.loads(request.body)
    customer = request.user.customer
    position = data['form']['position']
    phone_number = data['form']['phone']
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    total = order.get_cart_total
    order.transaction_id = str(transaction_id) + f' @ {position}'
    order.position = position
    order.phone = phone_number

    if int(total) == int(order.get_cart_total):
        order.complete = True
    order.save()

    # ItemsOrdered.product = OrderItem.product
    # ItemsOrdered.quantity = OrderItem.quantity
    # ItemsOrdered.position = Order.position
    # ItemsOrdered.save(self)

    print('Data;', request.body)
    return JsonResponse('Placed orders', safe=False)

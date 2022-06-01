from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    id = models.IntegerField(primary_key=True)


class Product(models.Model):
    name = models.CharField(max_length=255, null=True)
    price = models.IntegerField(null=False)
    stock = models.IntegerField()
    image = models.ImageField(null=True, blank=True)
    category = models.CharField(max_length=35, null=True)

    def __str__(self):
        return self.name

    @property
    def imageUrl(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Order(models.Model):  # adding & removing items to shopping cart
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)  # remove this
    position = models.CharField(max_length=15, null=False)
    date = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    phone = models.IntegerField(default=0)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.date)

    @property
    def get_cart_total(self):
        order_items = self.orderitem_set.all()
        total = sum([item.get_total for item in order_items])
        return total

    @property
    def get_cart_items(self):
        order_items = self.orderitem_set.all()
        total = sum(item.quantity for item in order_items)
        return total


class OrderItem(models.Model):  # placing an order for selected items
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total

    @property
    def get_quantity(self):
        for x in self.product.name:
            quantity = self.quantity
        return quantity


class Shipping(models.Model):  # shipping for remote order
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=30)
    house_number = models.CharField(max_length=40)
    building = models.CharField(max_length=45)

    def __str__(self):
        return self.address


# class OrderMade(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
#     position = models.CharField(max_length=15, null=False)

class ItemsOrdered(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    position = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)


class Report(models.Model):
    name = models.CharField(max_length=255, null=True)
    month = models.IntegerField(default=0, null=True, blank=True)
    items_sold = models.IntegerField(default=0, null=True, blank=True)


class Chart(models.Model):
    month = models.IntegerField(default=0, null=True, blank=True)
    total = models.IntegerField(default=0, null=True, blank=True)
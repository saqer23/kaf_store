from django.db import models
from shop.models import Product

class Order(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone_no = models.IntegerField()
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=70)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering=('-created',)
        verbose_name = 'order'
        verbose_name_plural = "orders"
    def __str__(self):
        return "رقم الطلب {}".format(self.id)
    def get_total_cost(self):
        return sum(item.get_cost() for item in self.item.all())


class OrderItem(models.Model):
    Order = models.ForeignKey(Order,related_name='items',on_delete=models.CASCADE)
    product = models.ForeignKey(Product,related_name='order_item',on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=7,decimal_places=2)
    quamtity = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name = "OrderItem"
        verbose_name_plural = "OrderItems"
    def __str__(self):
        return '{}'.format(self.id)
    def get_cost(self):
        return self.price * self.quamtity
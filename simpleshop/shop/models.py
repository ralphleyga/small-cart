from django.db import models
from django.conf import settings

BAG = 1
PLACED_ORDER = 2
CANCELED = 3

ORDER_STATUS = (
    (BAG, 'Cart'),
    (PLACED_ORDER, 'Placed Order'),
    (CANCELED, 'Canceled'),
)


PENDING = 1
PROCESS_STATUS = (
    (PENDING, 'pending'),
    (2, 'confirm'),
    (3, 'packaging'),
    (4, 'pickup by logistic'),
    (5, 'shipping'),
    (6, 'delivered'),
)

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    def price_range(self):
        items = self.item_set.filter(product__id=self.id).order_by('price')
        first = round(items.first().price, 3)
        last = round(items.last().price, 3)
        return f'${first} - ${last}'

    def items(self):
        return self.item_set.all().order_by('price')


class Item(models.Model):
    title = models.CharField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.title

class GenericManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(archived=False)

class Address(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    apartment_address = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=100)
    default = models.BooleanField(default=False)
    archived = models.BooleanField(default=False)
    objects = GenericManager()
    
    def delete(self):
        self.archived = True
        super().save()

    def __str__(self):
        return self.full_address()

    def full_address(self):
        return f'{self.apartment_address}, {self.street_address}, {self.postal_code}'


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                on_delete=models.CASCADE)
    address = models.ForeignKey(Address, null=True, on_delete=models.DO_NOTHING)
    status = models.IntegerField(choices=ORDER_STATUS)
    process_status = models.IntegerField(choices=PROCESS_STATUS, blank=True, null=True)
    total_price = 0

    def total_items(self):
        """Total item in BAG

        TODO: to optimize using agregators
        """
        total = 0
        for item in self.orderitem_set.all():
            total += item.quantity
            self.total_price = float(self.total_price) + float(item.total_price)
        return total

    def total_prices(self):
        """Total item in BAG

        TODO: to optimize using agregators
        """
        self.total_items()
        return float(self.total_price)

    def __str__(self):
        return str(self.id)

class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    cart = models.ForeignKey(Order, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)

    @property
    def total_price(self):
        return self.item.price * self.quantity


class OrderShippingUpdate(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.order.id
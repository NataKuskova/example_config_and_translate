from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User, UserManager


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    photo = models.ImageField(default='None', upload_to='products_photo/')
    user = models.ForeignKey(User, null=True)

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'id': self.pk})


class Buyer(models.Model):
    # user = models.OneToOneField(
    #     User,
    #     on_delete=models.CASCADE,
    #     primary_key=True
    # )
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=19)

    # objects = UserManager()

    def __str__(self):
        return '%s %s' % (self.name, self.surname)


class Order(models.Model):
    user = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    date_order = models.DateTimeField()
    sum = models.DecimalField(max_digits=10, decimal_places=2)
    products = models.ManyToManyField(Product, through='ListOfOrder')

    def __str__(self):
        return str(self.user)


class ListOfOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    sum = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return '%s, %s, %s, %s, %s' % \
               (self.order, self.product, self.price, self.quantity,
                self.sum)

    class Meta:
        unique_together = (('order', 'product'),)

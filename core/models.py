from django.db import models
from django.utils import timezone


STATEMENT_TYPE = [
    ("Quote", "Quote"),
    ("Order", "Order"),
    ("Invoice", "Invoice"),
]

class Supplier(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
class ComponentType(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
class Component(models.Model):
    name = models.CharField(max_length=50)
    component_type = models.ForeignKey(ComponentType, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
class PurchaseOrder(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
class Stock(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    tax = models.FloatField(default=5)
    component = models.ManyToManyField(Component)
    def __str__(self):
        return self.name
class Customer(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
class Statement(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, unique=True)
    statement_type = models.CharField(max_length=50, choices=STATEMENT_TYPE, default='Quote')
    is_canceled = models.BooleanField()
    def __str__(self):
        return f"Statement for {self.customer}"
class StatementLine(models.Model):
    statement = models.ForeignKey(Statement, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField(default=1)
    def __str__(self):
        return f"{self.statement} with product {self.product}"
    @property
    def total(self):
        return (self.price * self.quantity * (100 + self.product.tax)/100)

class SaleOrder(models.Model):
    statement = models.ForeignKey(Statement, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return f"SO: {self.statement} at {self.date}"
class Quotation(models.Model):
    statement = models.ForeignKey(Statement, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return f"Quotation: {self.statement} at {self.date}"
class Invoice(models.Model):
    statement = models.ForeignKey(Statement, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    discount = models.FloatField()
    def __str__(self):
        return f"Invoice: {self.statement} at {self.date}"
class Inventory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    def __str__(self):
        return f"{self.product}: {self.quantity}"
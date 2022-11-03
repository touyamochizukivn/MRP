from django.db import models
from django.utils import timezone


QUOTATION_STATUS = [
    ("Draft", "Draft"),
    ("Pending", "Pending"),
    ("Confirm", "Confirm"),
    ("Refuse", "Refuse"),
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

class Quotation(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=QUOTATION_STATUS, default='Draft')
    date = models.DateTimeField(default=timezone.now)
    comment = models.CharField(max_length=50, null=True, blank=True)
    def __str__(self):
        return f"Quotation: {self.customer} at {self.date}"
class QuotationLine(models.Model):
    quotation = models.ForeignKey(Quotation, on_delete=models.CASCADE, related_name='quotation_lines')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField(default=1)
    def __str__(self):
        return f"QuotationLine: {self.quotation.customer} - {self.product}"
    @property
    def total(self):
        return (self.price * self.quantity * (100 + self.product.tax)/100)
class SaleOrder(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quotation = models.ForeignKey(Quotation, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return f"SaleOrder: {self.customer} at {self.date}"
class SaleOrderLine(models.Model):
    sale_order = models.ForeignKey(SaleOrder, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField(default=1)
    def __str__(self):
        return f"SaleOrderLine: {self.sale_order} : {self.product}"
class Invoice(models.Model):
    sale_order = models.ForeignKey(SaleOrder, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    discount = models.FloatField()
    def __str__(self):
        return f"Invoice: {self.sale_order} at {self.date}"
class InvoiceLine(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField(default=1)
    def __str__(self):
        return f"InvoiceLine: {self.invoice} : {self.product}"


class Inventory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    def __str__(self):
        return f"{self.product}: {self.quantity}"
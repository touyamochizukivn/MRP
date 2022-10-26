from django.db import models


class Supplier(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
class Component(models.Model):
    name = models.CharField(max_length=50)
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
    def __str__(self):
        return self.name
class Customer(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
class StatementType(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
class Statement(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    statement_type = models.ForeignKey(StatementType, on_delete=models.CASCADE)
    is_canceled = models.BooleanField()
    def __str__(self):
        return f"Statement for {self.customer}"
class StatementLine(models.Model):
    statement = models.ForeignKey(Statement, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.IntegerField()

class SaleOrder(models.Model):
    statement = models.ForeignKey(Statement, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"SO: {self.statement} at {self.date}"
class Quote(models.Model):
    statement = models.ForeignKey(Statement, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Quote: {self.statement} at {self.date}"
class Invoice(models.Model):
    statement = models.ForeignKey(Statement, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    discount = models.FloatField()
    def __str__(self):
        return f"Invoice: {self.statement} at {self.date}"


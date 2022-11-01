from django.db import models

# Create your models here.
class Parent(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    


class Child(models.Model):
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    def __str__(self):
        return f"{self.parent.name} - {self.name}"
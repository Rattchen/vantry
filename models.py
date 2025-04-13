from django.db import models

class Storage(models.Model):
    """A virtual storage for products, like a fridge, a freezer, a shelf or a kitchen cabinet."""
    name = models.CharField(max_length=250)
    color = models.CharField(max_length=7, null=True, blank=True) #If someone wants to color-code their cabinets

    def __str__(self):
        return self.name

class Product(models.Model):
    barcode = models.PositiveBigIntegerField(null=True, blank=True)
    brand = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    calories = models.PositiveIntegerField()
    expiry_date = models.DateField(null=True, blank=True)
    quantity = models.PositiveIntegerField(null=True, blank=True)
    storage = models.ForeignKey(Storage, on_delete=models.CASCADE, related_name="products")

    def __str__(self):
        return f"{self.name} by {self.brand}"

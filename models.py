from django.db import models

class Product(models.Model):
    off_id = models.PositiveBigIntegerField(null=True, blank=True) #OpenFoodFacts ID used to fetch more data
    brand = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    calories = models.PositiveIntegerField()
    expiry_date = models.DateField(null=True, blank=True)
    quantity = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} by {self.brand}"
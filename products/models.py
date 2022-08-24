from django.db import models


class Product(models.Model):
    description = models.TextField()
    price = models.FloatField()
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)

    seller = models.ForeignKey(
        "accounts.Account", on_delete=models.CASCADE, related_name="products"
    )

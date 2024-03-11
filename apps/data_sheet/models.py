from django.db import models
from apps.product.models import Product


class DataSheet(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    principal = models.BooleanField(default=False)
    photo = models.ImageField(upload_to='media/data_sheet/', null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

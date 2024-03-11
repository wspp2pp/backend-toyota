from django.db import models
from apps.category.models import Category


class Product(models.Model):
    class Meta:
        verbose_name = 'Product'

    name = models.CharField(max_length=50)
    price = models.IntegerField()
    year = models.IntegerField()
    photo = models.ImageField(upload_to='media/product/', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

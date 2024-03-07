from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

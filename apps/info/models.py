from django.db import models


class Info(models.Model):
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=255)
    section = models.IntegerField()

    def __str__(self):
        return self.name

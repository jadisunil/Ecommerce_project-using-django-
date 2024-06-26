from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class meta:
        verbose_name = "Category"
        verbose_name_plural = "categories"

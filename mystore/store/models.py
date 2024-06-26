from django.db import models
from .category import Category
from django.contrib.auth.models import User



# Create your models here.

class product(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='img')
    desc = models.TextField()
    price = models.IntegerField()
    Category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name

    class meta:
        verbose_name = "product"
        verbose_name_plural = "products"

    # static method

    @staticmethod
    def get_category_id(get_id):
        if get_id:
            return product.objects.filter(Category=get_id)
        else:
            return product.objects.all()
        
        
# class CartItem(models.Model):
#     product = models.ForeignKey(product, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(default=0)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     date_added = models.DateTimeField(auto_now_add=True)
 
#     def __str__(self):
#         return f'{self.quantity} x {self.product.name}'
    
#     class meta:
#         verbose_name = "cartitem"
#         verbose_name_plural = "cartitems"
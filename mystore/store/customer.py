from django.db import models

from .models import models
from .category import Category



class customer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=10)
    password = models.CharField(max_length=200)

    # checking email is exist or not 
    def isexit(self):
        if customer.objects.filter(email=self.email):
            return True 
        return False
    
 
    @staticmethod
    def getmail(email):
        try:
            return customer.objects.get(email=email)
        except customer.DoesNotExist:
            return None
            
            
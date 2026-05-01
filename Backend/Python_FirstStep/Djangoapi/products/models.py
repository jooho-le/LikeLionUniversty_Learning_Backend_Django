from django.db import models

class Product(models.Model):
    product_name = models.CharField(max_length=100, blank=False, default="")
    price = models.DecimalField(max_digits=20, decimal_places=1, blank=False, default=0) # max_digits는 총 자릿수, decimal_places는 소수점 이하 자릿수
    
    

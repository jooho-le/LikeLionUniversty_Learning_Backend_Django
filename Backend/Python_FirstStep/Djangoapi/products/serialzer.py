from rest_framework import serializers
from products.models import Product

class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
    
        model = Product
    
        fields = { # initial 참고 
            'id',
            'product_name',
            'price',
        }
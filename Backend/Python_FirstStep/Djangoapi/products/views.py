from rest_framework.viewsets import ModelViewSet
from .serialzer import ProductSerializer
from .models import Product

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all() # Product 모델의 모든 객체를 가져옴
    serializer_class = ProductSerializer # ProductSerializer를 사용하여 직렬화/역직렬화
    
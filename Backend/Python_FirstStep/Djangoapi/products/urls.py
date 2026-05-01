# 뷰 셋 등록 

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('product', views.ProductViewSet) # product이라는 URL 경로에 ProductViewSet을 등록

urlpatterns = [
    path('', include(router.urls)), # router가 등록된 URL 패턴을 포함
]

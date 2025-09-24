from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, crypto_prices, product_chart, crypto_chart, api_root  # import all views including api_root

router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', api_root),                        # API Root with clickable links
    path('crypto-prices/', crypto_prices),    # endpoint for raw crypto prices API
    path('product-chart/', product_chart),    # endpoint for product prices chart
    path('crypto-chart/', crypto_chart),      # endpoint for crypto prices chart
    path('', include(router.urls)),           # CRUD APIs for products
]
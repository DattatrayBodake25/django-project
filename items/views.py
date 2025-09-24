from django.shortcuts import render
from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
import plotly.express as px
import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.urls import reverse

# -----------------------------
# CRUD API for Products
# -----------------------------
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# -----------------------------
# Third-Party API: Crypto Prices (raw JSON)
# -----------------------------
@api_view(['GET'])
def crypto_prices(request):
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        'ids': 'bitcoin,ethereum,ripple,cardano,dogecoin,polkadot,binancecoin,solana,shiba-inu,litecoin',
        'vs_currencies': 'usd'
    }
    response = requests.get(url, params=params)
    data = response.json()
    return Response(data)

# -----------------------------
# Data Visualization: Crypto Prices Chart
# -----------------------------
def crypto_chart(request):
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        'ids': 'bitcoin,ethereum,ripple,cardano,dogecoin,polkadot,binancecoin,solana,shiba-inu,litecoin',
        'vs_currencies': 'usd'
    }
    response = requests.get(url, params=params)
    data = response.json()

    names = list(data.keys())
    prices = [data[name]['usd'] for name in names]

    fig = px.bar(
        x=names,
        y=prices,
        labels={'x': 'Crypto', 'y': 'Price (USD)'},
        title="Top 10 Crypto Prices"
    )
    chart = fig.to_html(full_html=False)
    return render(request, "items/crypto_chart.html", {"chart": chart})

# -----------------------------
# Data Visualization: Product Prices Chart
# -----------------------------
def product_chart(request):
    products = Product.objects.all()
    names = [p.name for p in products]
    prices = [p.price for p in products]

    fig = px.bar(
        x=names,
        y=prices,
        labels={'x': 'Product', 'y': 'Price'},
        title="Product Prices"
    )
    chart = fig.to_html(full_html=False)
    return render(request, "items/product_chart.html", {"chart": chart})

# -----------------------------
# API Root: clickable endpoints
# -----------------------------
@api_view(['GET'])
def api_root(request):
    """
    Custom API root returning all endpoints as clickable links.
    """
    return Response({
        "message": "Welcome to DemoApp API!",
        "api_root": request.build_absolute_uri('/api/'),
        "endpoints": {
            "Product CRUD": {
                "List / Create": request.build_absolute_uri(reverse('product-list')),
                "Detail / Update / Delete (example ID=1)": request.build_absolute_uri('/api/products/1/')
            },
            "Product Chart": request.build_absolute_uri('/api/product-chart/'),
            "Crypto Prices API": request.build_absolute_uri('/api/crypto-prices/'),
            "Crypto Chart": request.build_absolute_uri('/api/crypto-chart/')
        }
    })

from django.shortcuts import render
from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
import plotly.express as px
import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.urls import reverse
from django.core.cache import cache
from datetime import timedelta

# -----------------------------
# CRUD API for Products
# -----------------------------
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# -----------------------------
# Third-Party API: Crypto Prices (raw JSON) with caching
# -----------------------------
@api_view(['GET'])
def crypto_prices(request):
    # Try fetching cached data first
    cached_data = cache.get('crypto_prices')
    if cached_data:
        return Response(cached_data)

    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        'ids': 'bitcoin,ethereum,ripple,cardano,dogecoin,polkadot,binancecoin,solana,shiba-inu,litecoin',
        'vs_currencies': 'usd'
    }

    try:
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()
        data = response.json()

        # Check if API returned a rate-limit error
        if "error_code" in data:
            return Response({"error": "Rate limit exceeded. Please try again later."}, status=429)

        # Cache the result for 5 minutes
        cache.set('crypto_prices', data, timeout=300)
        return Response(data)

    except requests.RequestException as e:
        return Response({"error": "Failed to fetch crypto prices.", "details": str(e)}, status=503)

# -----------------------------
# Data Visualization: Crypto Prices Chart
# -----------------------------
def crypto_chart(request):
    cached_data = cache.get('crypto_prices')
    if cached_data:
        data = cached_data
    else:
        # Fetch fresh data if cache is empty
        url = "https://api.coingecko.com/api/v3/simple/price"
        params = {
            'ids': 'bitcoin,ethereum,ripple,cardano,dogecoin,polkadot,binancecoin,solana,shiba-inu,litecoin',
            'vs_currencies': 'usd'
        }
        try:
            response = requests.get(url, params=params, timeout=5)
            response.raise_for_status()
            data = response.json()
            if "error_code" in data:
                return render(request, "items/error.html", {"message": "Rate limit exceeded. Please try again later."})
            cache.set('crypto_prices', data, timeout=300)
        except requests.RequestException as e:
            return render(request, "items/error.html", {"message": f"Failed to fetch crypto prices: {e}"})

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

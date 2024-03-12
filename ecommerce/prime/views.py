from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from prime.models import Product, Category, Order, OrderItem, Address
from prime.serializers import ProductSerializer, CategorySerializer, OrderSerializer, OrderItemSerializer, AddressSerializer


class ProductList(APIView):
    def get(self, request):
        data = {'message': 'Hello, World!'}
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

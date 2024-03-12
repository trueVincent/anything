from rest_framework import serializers

from prime.models import Product, Category, Order, OrderItem, Address


class ProductSerializer(serializers.Serializer):
    class Meta:
        model = Product
        fields = '__all__'


class CategorySerializer(serializers.Serializer):
    class Meta:
        model = Category
        fields = '__all__'


class OrderSerializer(serializers.Serializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderItemSerializer(serializers.Serializer):
    class Meta:
        model = OrderItem
        fields = '__all__'


class AddressSerializer(serializers.Serializer):
    class Meta:
        model = Address
        fields = '__all__'

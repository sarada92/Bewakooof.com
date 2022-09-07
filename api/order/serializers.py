from rest_framework import serializers
from .models import Order


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ('transaction_id', 'user', 'product_id',
                  'total_products', 'total_amount')
        # TODO: add product and quantity

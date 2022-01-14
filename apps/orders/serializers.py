from rest_framework import serializers

from clients.serializers import ClientSerializer
from drivers.serializers import DriverSerializer
from orders.models import Order


class OrderListSerializer(serializers.ModelSerializer):
    client = ClientSerializer()
    driver = DriverSerializer()

    class Meta:
        model = Order
        fields = [
            'client',
            'driver',
            'status',
            'start_point_lat',
            'start_point_long',
            'end_point_lat',
            'end_point_long',
            'amount',
        ]


class OrderCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'client',
            'driver',
            'status',
            'start_point_lat',
            'start_point_long',
            'end_point_lat',
            'end_point_long',
            'amount',
        ]
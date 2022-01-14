from rest_framework import serializers
from rest_framework.exceptions import ValidationError

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

    def update(self, instance, validated_data):
        if instance.status in (Order.CANCELED, Order.FINISHED):
            raise ValidationError({'permission denied': "Can't update after order completed"})

        if self.context['request'].user.id == instance.client.user.id:
            if instance.status == Order.CREATED and validated_data.get('status') == Order.CANCELED:
                return super().update(instance, validated_data)

        if self.context['request'].user.id == instance.driver.user.id:
            if instance.status == Order.CREATED and validated_data.get('status') == Order.ACCEPTED:
                return super().update(instance, validated_data)
            elif instance.status == Order.ACCEPTED and validated_data.get('status') == Order.FINISHED:
                return super().update(instance, validated_data)

        raise ValidationError({'permission denied': "Can't update status"})

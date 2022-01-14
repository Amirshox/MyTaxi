from rest_framework import serializers

from drivers.models import Car, Driver
from users.serializers import UserModelSerializer


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = [
            'id',
            'number',
            'model',
            'color',
            'seria_number',
        ]


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = [
            'id',
            'user',
            'car',
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user'] = UserModelSerializer(instance.user).data
        representation['car'] = CarSerializer(instance.car).data
        return representation

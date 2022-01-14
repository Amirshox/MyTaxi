from rest_framework import serializers

from clients.models import Client
from users.serializers import UserModelSerializer


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = [
            'id',
            'user',
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user'] = UserModelSerializer(instance.user).data
        return representation

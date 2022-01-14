from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from clients.models import Client
from clients.serializers import ClientSerializer
from orders.serializers import OrderListSerializer


class ClientViewSet(GenericViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    @action(methods=['get'], detail=True)
    def orders(self, request, pk=None):
        client = self.get_object()
        # orders = client.orders.filter_queryset()
        orders = client.orders.all()
        serializer = OrderListSerializer(orders, many=True)
        return Response(serializer.data)

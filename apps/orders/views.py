from django.shortcuts import render
from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.viewsets import GenericViewSet

from orders.models import Order
from orders.serializers import OrderListSerializer, OrderCreateUpdateSerializer


class OrderViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update':
            return OrderCreateUpdateSerializer
        return super().get_serializer_class()

    def perform_create(self, serializer):
        serializer.save(client_id=self.request.user.id)

    # @action(methods=['get'], detail=True)
    # def free_clients

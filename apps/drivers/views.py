from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from drivers.models import Car, Driver
from drivers.serializers import CarSerializer, DriverSerializer
from orders.serializers import OrderListSerializer


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer

    @action(methods=['get'], detail=True)
    def search_orders(self, request, pk=None):
        driver = self.get_object()
        orders = driver.orders.filter(status='CREATED')
        serializer = OrderListSerializer(orders, many=True)
        return Response(serializer.data)

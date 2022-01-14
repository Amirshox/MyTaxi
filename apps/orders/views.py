from datetime import datetime

from django.shortcuts import render
from rest_framework import viewsets, mixins, generics
from rest_framework.decorators import action
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from orders.models import Order
from orders.serializers import OrderListSerializer, OrderCreateUpdateSerializer


class OrderCreateViewSet(mixins.CreateModelMixin, GenericViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderCreateUpdateSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(client_id=self.request.user.id)


class OrderUpdateViewSet(mixins.UpdateModelMixin, GenericViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderCreateUpdateSerializer


class OrderListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer

    # @action(methods=['get'], detail=True)
    # def search_orders(self, request, pk=None):
    #     driver = self.get_object()
    #     orders = driver.orders.filter(status='CREATED')
    #     serializer = OrderListSerializer(orders, many=True)
    #     return Response(serializer.data)


class OrderListApiView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer

    def get_queryset(self):
        client_id = self.kwargs['pk']
        queryset = self.queryset.filter(client_id=client_id)
        from_date = self.request.query_params.get('from')
        to_date = self.request.query_params.get('to')

        if from_date:
            queryset = queryset.filter(modified_date__gte=datetime.strptime(from_date, '%Y-%d-%m'))
        if to_date:
            queryset = queryset.filter(modified_date__lte=datetime.strptime(to_date, '%Y-%d-%m'))
        return queryset

from datetime import datetime

from rest_framework import mixins
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from orders.models import Order
from orders.serializers import OrderListSerializer, OrderCreateUpdateSerializer

DATE_FORMAT = "%Y-%d-%m"


class OrderCreateViewSet(mixins.CreateModelMixin, mixins.UpdateModelMixin, GenericViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderCreateUpdateSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(client_id=self.request.user.id)


class OrderListApiView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer

    def get_queryset(self):
        client_id = self.kwargs.get('pk')
        from_date, to_date = self.get_dates(self.request.query_params)
        queryset = self._filter_queryset(self.queryset, from_date, to_date, client_id)
        return queryset

    @staticmethod
    def _filter_queryset(queryset, from_date, to_date, client_id):
        if client_id:
            queryset = queryset.filter(client_id=client_id)
        if from_date:
            queryset = queryset.filter(modified_date__date__gte=from_date)
        if to_date:
            queryset = queryset.filter(modified_date__date__lte=to_date)
        return queryset

    @staticmethod
    def get_dates(query_params):
        from_date, to_date = query_params.get('from'), query_params.get('to')
        try:
            from_date = datetime.strptime(from_date, DATE_FORMAT)
        except:
            from_date = None
        try:
            to_date = datetime.strptime(to_date, DATE_FORMAT)
        except:
            to_date = None
        return from_date, to_date

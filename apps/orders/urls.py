from django.urls import path
from rest_framework import routers

from orders.views import OrderCreateViewSet, OrderListApiView

router = routers.DefaultRouter()

router.register('orders', OrderCreateViewSet)

urlpatterns = [
    path('orders/client/<int:pk>/', OrderListApiView.as_view())
]

urlpatterns += router.urls

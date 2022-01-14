from django.urls import path
from rest_framework import routers

from orders.views import OrderCreateViewSet, OrderUpdateViewSet, OrderListApiView

router = routers.DefaultRouter()

router.register('create', OrderCreateViewSet)
router.register('update-status', OrderUpdateViewSet)

urlpatterns = [
    path('client/<int:pk>/', OrderListApiView.as_view())
]

urlpatterns += router.urls

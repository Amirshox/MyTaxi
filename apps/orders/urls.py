from rest_framework import routers

from orders.views import OrderViewSet

router = routers.DefaultRouter()

router.register('order', OrderViewSet)

urlpatterns = router.urls

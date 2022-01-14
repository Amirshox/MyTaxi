from rest_framework import routers

from drivers.views import CarViewSet, DriverViewSet

router = routers.DefaultRouter()

router.register('driver', DriverViewSet)
router.register('car', CarViewSet)

urlpatterns = router.urls

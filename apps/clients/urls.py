from rest_framework import routers

from clients.views import ClientViewSet

router = routers.DefaultRouter()

# router.register('client', ClientViewSet)

urlpatterns = router.urls

from rest_framework import routers

from users.views import UserViewSet

router = routers.DefaultRouter()

router.register('user', UserViewSet)

urlpatterns = router.urls

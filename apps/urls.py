from django.urls import path, include

api_v = 'api/v1/'

urlpatterns = [
    path(api_v + 'users/', include(('users.urls', 'users'), 'users')),
    path(api_v + 'clients/', include(('clients.urls', 'clients'), 'client')),
    path(api_v + 'orders/', include(('orders.urls', 'orders'), 'orders')),
    path(api_v + 'drivers/', include(('drivers.urls', 'drivers'), 'drivers')),
]

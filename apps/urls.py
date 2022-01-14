from django.urls import path, include

urlpatterns = [
    path('users/', include(('users.urls', 'users'), 'users')),
    path('clients/', include(('clients.urls', 'clients'), 'client')),
    path('orders/', include(('orders.urls', 'orders'), 'orders')),
    path('drivers/', include(('drivers.urls', 'drivers'), 'drivers')),
]

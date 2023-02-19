from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet, GroupViewSet
from cliente.views import ClienteViewSet, PedidoViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'clientes', ClienteViewSet)
router.register(r'pedidos', PedidoViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

from rest_framework import viewsets
from rest_framework import permissions, authentication
from .serializers import ClienteSerializer, PedidoSerializer
from .models import Cliente, Pedido


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()

    serializer_class = ClienteSerializer
    #permission_classes = [permissions.IsAuthenticated]
    #authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]


class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all().order_by('-data')
    lookup_field = 'id' 
    serializer_class = PedidoSerializer
    #permission_classes = [permissions.IsAuthenticated]
    #authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]
# Create your views here.

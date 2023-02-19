from .models import Cliente, Pedido
from rest_framework import serializers


class PedidoSerializer(serializers.HyperlinkedModelSerializer):    
    cliente_nome = serializers.CharField(source='cliente.nome', read_only=True)
    class Meta:
        model = Pedido
        fields = ['id','cliente', 'cliente_nome' ,'data', 'qnt_marmita', 'valor_marmita', 'descricao', 'total', 'is_pago']
        read_only_fields = ['total']


class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    pedido_set = PedidoSerializer(many=True, read_only=True)
    class Meta:
        model = Cliente
        fields = ['id', 'nome', 'endereco', 'telefone', 'debito', 'pedido_set']
        read_only_fields = ['debito']
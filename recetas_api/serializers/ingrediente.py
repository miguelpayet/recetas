from rest_framework import serializers

from recetas.models import Ingrediente
from recetas.models import Insumo


class InsumoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Insumo
        fields = ['idinsumo', 'nombre']


class IngredienteSerializer(serializers.HyperlinkedModelSerializer):
    insumo = InsumoSerializer(required=True)

    class Meta:
        model = Ingrediente
        fields = ['idingrediente', 'insumo', 'indicaciones']

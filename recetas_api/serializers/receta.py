from rest_framework import serializers

from recetas.models import Receta


class RecetaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Receta
        fields = ['idreceta', 'nombre', 'porciones']


class InstruccionesRecetaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Receta
        fields = ['instrucciones']

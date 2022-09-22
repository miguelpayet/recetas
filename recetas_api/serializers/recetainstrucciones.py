from rest_framework import serializers

from recetas.models import Receta


class RecetaInstruccionesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Receta
        fields = ['instrucciones']

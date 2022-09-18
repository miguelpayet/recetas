from rest_framework import serializers

from recetas_app.models import Receta


class RecetaSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Receta
        fields = ['idreceta', 'nombre', 'porciones']

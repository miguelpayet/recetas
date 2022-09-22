from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from recetas_api.serializers.receta import RecetaSerializer
from recetas.models import Receta
from recetas_api.serializers import IngredienteSerializer
from recetas_api.serializers import RecetaInstruccionesSerializer


class RecetaViewSet(viewsets.ModelViewSet):
    queryset = Receta.objects.all().order_by('idreceta')
    serializer_class = RecetaSerializer

    @action(detail=True, methods=['GET'])
    def ingredientes(self, request, pk=None):
        user = self.get_object()
        receta = Receta.objects.get(idreceta=pk)
        ingredientes = receta.ingrediente_set.all()
        serializer = IngredienteSerializer(ingredientes, many=True, context={'request': request})
        return Response(serializer.data)

    @action(detail=True, methods=['GET'])
    def instrucciones(self, request, pk=None):
        user = self.get_object()
        receta = Receta.objects.get(idreceta=pk)
        serializer = RecetaInstruccionesSerializer(receta, many=False, context={'request': request})
        return Response(serializer.data)

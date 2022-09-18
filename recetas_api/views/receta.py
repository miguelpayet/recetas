from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import action

from recetas_api.serializers.receta import RecetaSerializer
from recetas_app.models.receta import Receta


class RecetaViewSet(viewsets.ModelViewSet):
    queryset = Receta.objects.all().order_by('idreceta')
    serializer_class = RecetaSerializer

    @action(detail=True, methods=['post'])
    def ingredientes(self, request, pk=None):
        user = self.get_object()
        serializer = IngredientesSerializer(data=request.data)
        if serializer.is_valid():
            user.set_password(serializer.validated_data['password'])
            user.save()
            return Response({'status': 'password set'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

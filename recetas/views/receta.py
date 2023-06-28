from django.views.generic import TemplateView

from recetas.models.receta import Receta


class RecetaView(TemplateView):
    template_name = "recetas/receta.html"

    def get_context_data(self, **kwargs):
        idreceta = self.kwargs['idreceta']
        receta = Receta.objects.get(idreceta=idreceta)
        return {'receta': receta}

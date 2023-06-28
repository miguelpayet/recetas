from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from recetas.views import index
from recetas.views import RecetaView

urlpatterns = [
                  path('', index, name="index"),
                  path('receta/<int:idreceta>/', RecetaView.as_view(), name="recetas"),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import include
from django.urls import path
from rest_framework import routers
from recetas_api.views.receta import RecetaViewSet

router = routers.DefaultRouter()
router.register(r'recetas', RecetaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

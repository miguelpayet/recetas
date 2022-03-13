from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from admin_app.views import admin_index

from recetas_app.views import index_view

urlpatterns = [
                  path('', index_view, name="index"),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

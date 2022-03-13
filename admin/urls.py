from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from admin_app.views import admin_index

urlpatterns = [
                  path('', admin_index, name="index"),
                  path('admin', admin.site.urls, name="admin"),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from admin.views import admin_index
from django.conf.urls import include

urlpatterns = [
                  path('', admin_index, name="index"),
                  path('admin', admin.site.urls, name="admin"),
                  path('grappelli/', include('grappelli.urls')),  # grappelli URLS
                  path('_nested_admin/', include('nested_admin.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('api/category/', include('apps.category.urls', namespace='category')),
                  path('api/product/', include('apps.product.urls', namespace='product')),
                  path('api/data-sheet/', include('apps.data_sheet.urls', namespace='data_sheet')),
                  path('api/info/', include('apps.info.urls', namespace='info')),

                  path('admin/', admin.site.urls),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

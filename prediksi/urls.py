from django.urls import path, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from .views import PermintaanIkanViewSet, prediksi_permintaan
from .views import home

router = DefaultRouter()
router.register(r'permintaan', PermintaanIkanViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('prediksi.urls')),
    path('', include('prediksi.urls')),
    path('', home, name='home'),
    path('permintaan/', PermintaanIkanViewSet.as_view({'get': 'list'})),
    path('', include(router.urls)),
    path('prediksi/', prediksi_permintaan),
]

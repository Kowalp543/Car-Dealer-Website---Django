from django.urls import path
from . import views
from .views import SamochodCreateView, offer_img, export_csv
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('search/<int:price_min>/<int:price_max>/<str:marka>', views.search, name='oferty'),
    path('add/', SamochodCreateView.as_view(), name='samochod_add'),
    path('export/', export_csv, name='export_csv'),
    path('img/', offer_img, name='offer_img'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

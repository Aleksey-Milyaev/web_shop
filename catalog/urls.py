from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import get_home, contacts

app_name = CatalogConfig.name

urlpatterns = [
    path('', get_home, name='home'),
    path('contacts/', contacts, name='contacts'),
]

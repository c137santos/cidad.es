from django.urls import path

from . import views

urlpatterns = [
    path("search/", views.search),
    path("search/municipio/", views.search_municipio),
    path("uf/<id_ibge>/detail/", views.uf_detail),
    path("municipio/<id_ibge>/detail/", views.municipio_detail),
    path("uf/<id_ibge>/municipios/", views.list_municipios),
]

from .models import UF, Municipio
from django.http import JsonResponse

def search(request):
    pass


def search_municipio(request):
    pass

def uf_detail(request, id_ibge):
    uf = UF.objects.get(id_ibge=id_ibge)
    response = JsonResponse(uf.to_dict_json())
    return response


def list_municipios(request, id_ibge):
    id_ibge_uf = id_ibge
    municipios = Municipio.objects.filter(uf_id=id_ibge_uf)
    response = JsonResponse({"resultados":[
        municipio.to_dict_json() for municipio in municipios
    ]})
    return response


    # Quais objetos dentro do python pode virar um jsonResponse? Dicionários. Dentro de classe é metodo.


def municipio_detail(request, id_ibge):
    municipio = Municipio.objects.get(id_ibge=id_ibge)
    response = JsonResponse(municipio.to_dict_json())
    return response
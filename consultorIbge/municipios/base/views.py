from .models import UF, Municipio
from django.http import JsonResponse
from django.db.models import Q

def search(request):
    qtext = request.GET.get("q")
    q = Q(nome__icontains=qtext) | Q(id_ibge=qtext) | Q(sigla=qtext)
    ufs = UF.objects.filter(q)
    response = JsonResponse({'resultados': [uf.to_dict_json() for uf in ufs]})
    return response


def search_municipio(request):
    qtext = request.GET.get("q")
    q = Q(nome__icontains=qtext) | Q(id_ibge=qtext) | Q(uf_sigla=qtext)
    municipios = Municipio.objects.filter(q)
    response = JsonResponse({'resultados': [municipio.to_dict_json() for municipio in municipios]})
    return response

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


def municipio_detail(request, id_ibge):
    municipio = Municipio.objects.get(id_ibge=id_ibge)
    response = JsonResponse(municipio.to_dict_json())
    return response
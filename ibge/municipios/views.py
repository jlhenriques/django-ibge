
from .models import Municipio, MesoRegiao, REGIOES, UFS
from .models import DIC_REGIOES_UFS

from django import http
from django.views.generic.list import ListView

from localflavor.br import br_states

class HomeListView(ListView):
    queryset = [dict(id=id, nome=nome) for id, nome in REGIOES]
    template_name='municipios/home.html'

def uf_list_view(request, cod_reg):
    ufs_da_regiao = DIC_REGIOES_UFS[int(cod_reg)]
    ufs = [dict(id=sigla, nome=nome)
            for sigla, nome in br_states.STATE_CHOICES
            if sigla in ufs_da_regiao]
    context = {'object_list': ufs}
    return http.JsonResponse(context)

def meso_regiao_list_view(request, uf):
    res = MesoRegiao.objects.filter(uf=uf)
    mesos = []
    for registro in res:
        mesos.append({'id':registro.id, 'nome':registro.nome})
    context = {'object_list': mesos}
    return http.JsonResponse(context)

def municipio_list_view(request, meso):
    res = Municipio.objects.filter(meso_regiao=meso)
    munis = []
    for registro in res:
        munis.append({'id':registro.id, 'nome':registro.nome})
    context = {'object_list': munis}
    return http.JsonResponse(context)

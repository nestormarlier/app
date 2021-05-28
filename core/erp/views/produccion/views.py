from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from django.views.generic import ListView


from core.erp.mixins import ValidatePermissionRequiredMixin

from core.erp.models import Impresora

class ProduccionListView(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):
    model = Impresora
    template_name = 'produccion/list.html'
    permission_required = 'erp.view_produccion'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        impresoras = {}
        try:
            action = request.POST['action']
            if action == "searchdata":
                impresoras=[]
                for i in Impresora.objects.filter(activo=True):
                    impresoras.append(i.toJSON())
            else:
                impresoras['error'] = 'Ha ocurrido un error'
        except Exception as e:
            impresoras['error'] = str(e)
        return JsonResponse(impresoras, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Impresoras'
        context['create_url'] = reverse_lazy('erp:index')
        context['list_url'] = reverse_lazy('erp:produccion_list')
        context['entity'] = 'Impresoras'
        return context


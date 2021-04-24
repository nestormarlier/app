from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from django.views.generic import CreateView

from core.erp.forms import ParteForm
from core.erp.mixins import ValidatePermissionRequiredMixin

from core.erp.models import OrdenesProduccion, ParteImpresion

class ParteCreateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
    model = ParteImpresion
    form_class = ParteForm
    template_name = 'parte/create.html'
    success_url = reverse_lazy('index')
    permission_required = 'erp.add_sale'
    url_redirect = success_url

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in OrdenesProduccion.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)
        #para que se pueda serializar debo especificar cuando es coleccion de elementos que el safe sea igual a False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de un parte de producción'
        context['entity'] = 'Parte'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context
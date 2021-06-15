from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView

from core.erp.mixins import ValidatePermissionRequiredMixin
from core.erp.models import FichaTecnica


class FichaView(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):
    model = FichaTecnica
    template_name = 'ficha/ficha.html'
    permission_required = 'erp.add_parte'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in FichaTecnica.objects.filter(id=self.kwargs.get('id')):
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Ficha técnica'
        context['entity'] = 'Fichas'
        # context['list_url'] = self.success_url
        context['action'] = 'searchdata'
        return context
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic import UpdateView, DeleteView, CreateView

from apps.registro_hora_extra.forms import RegistroHoraExtraForm

from .models import RegistroHoraExtra


class RegistroHoraExtraListView(ListView):
    model = RegistroHoraExtra
    paginate_by: int = 40

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return RegistroHoraExtra.objects.filter(funcionario__empresa=empresa_logada)


class RegistroHoraExtraUpdateView(UpdateView):
    model = RegistroHoraExtra
    form_class = RegistroHoraExtraForm

    def get_form_kwargs(self):
        kwargs = super(RegistroHoraExtraUpdateView, self).get_form_kwargs()
        kwargs.update({"usuario_injetado": self.request.user})
        return kwargs


class RegistroHoraExtraDeleteView(DeleteView):
    model = RegistroHoraExtra
    success_url: str = reverse_lazy("list_registro_hora_extra")


class RegistroHoraExtraCreateView(CreateView):
    model = RegistroHoraExtra
    form_class = RegistroHoraExtraForm

    def get_form_kwargs(self):
        kwargs = super(RegistroHoraExtraCreateView, self).get_form_kwargs()
        kwargs.update({"usuario_injetado": self.request.user})
        return kwargs

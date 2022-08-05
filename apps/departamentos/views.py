from django.contrib.auth.models import User
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic import UpdateView, DeleteView, CreateView

from .models import Departamento


class DepartamentoListView(ListView):
    model = Departamento
    paginate_by: int = 40

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Departamento.objects.filter(empresa=empresa_logada)


class DepartamentoUpdateView(UpdateView):
    model = Departamento
    fields = ["nome", ]


class DepartamentoDeleteView(DeleteView):
    model = Departamento
    success_url: str = reverse_lazy("list_departamentos")


class DepartamentoCreateView(CreateView):
    model = Departamento
    fields = ["nome", ]

    def form_valid(self, form) -> HttpResponse:
        departamento = form.save(commit=False)
        departamento.empresa = self.request.user.funcionario.empresa
        departamento.save()
        return super(DepartamentoCreateView, self).form_valid(form)

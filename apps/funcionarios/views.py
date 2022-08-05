from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic import UpdateView, DeleteView

from .models import Funcionario


class FuncionarioListView(ListView):
    model = Funcionario
    paginate_by: int = 40

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Funcionario.objects.filter(empresa=empresa_logada)


class FuncionarioUpdateView(UpdateView):
    model = Funcionario
    fields = ["nome", "departamento"]


class FuncionarioDeleteView(DeleteView):
    model = Funcionario
    success_url: str = reverse_lazy("list_funcionarios")

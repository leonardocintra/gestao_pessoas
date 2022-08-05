from django.contrib.auth.models import User
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic import UpdateView, DeleteView, CreateView

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


class FuncionarioCreateView(CreateView):
    model = Funcionario
    fields = ["nome", "departamento"]

    def form_valid(self, form) -> HttpResponse:
        funcionario = form.save(commit=False)

        username = funcionario.nome.split(
            ' ')[0] + funcionario.nome.split(' ')[1]
        funcionario.empresa = self.request.user.funcionario.empresa
        funcionario.user = User.objects.create(username=username)
        funcionario.save()
        return super(FuncionarioCreateView, self).form_valid(form)

from django.views.generic.list import ListView

from .models import Funcionario


class FuncionarioListView(ListView):
    model = Funcionario
    paginate_by: int = 40

from django.urls import path
from .views import FuncionarioUpdateView, FuncionarioListView

urlpatterns = [
    path("", FuncionarioListView.as_view(), name="list_funcionarios"),
    path("editar/<int:pk>", FuncionarioUpdateView.as_view(),
         name="update_funcionario"),
]

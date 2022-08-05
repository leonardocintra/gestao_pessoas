from django.urls import path
from .views import FuncionarioUpdateView, FuncionarioListView, FuncionarioDeleteView

urlpatterns = [
    path("", FuncionarioListView.as_view(), name="list_funcionarios"),
    path("delete/<int:pk>", FuncionarioDeleteView.as_view(), name="delete_funcionario"),
    path("editar/<int:pk>", FuncionarioUpdateView.as_view(),
         name="update_funcionario"),
]

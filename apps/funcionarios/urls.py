from django.urls import path
from .views import FuncionarioUpdateView, FuncionarioListView, FuncionarioDeleteView, FuncionarioCreateView

urlpatterns = [
    path("", FuncionarioListView.as_view(), name="list_funcionarios"),
    path("create/", FuncionarioCreateView.as_view(), name="create_funcionario"),
    path("delete/<int:pk>", FuncionarioDeleteView.as_view(), name="delete_funcionario"),
    path("editar/<int:pk>", FuncionarioUpdateView.as_view(),
         name="update_funcionario"),
]

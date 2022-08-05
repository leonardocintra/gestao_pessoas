from django.urls import path
from .views import DepartamentoUpdateView, DepartamentoListView, DepartamentoDeleteView, DepartamentoCreateView

urlpatterns = [
    path("", DepartamentoListView.as_view(), name="list_departamentos"),
    path("create/", DepartamentoCreateView.as_view(), name="create_departamento"),
    path("delete/<int:pk>", DepartamentoDeleteView.as_view(),
         name="delete_departamento"),
    path("editar/<int:pk>", DepartamentoUpdateView.as_view(),
         name="update_departamento"),
]

from django.urls import path
from .views import RegistroHoraExtraListView, RegistroHoraExtraUpdateView, RegistroHoraExtraDeleteView, RegistroHoraExtraCreateView

urlpatterns = [
    path("", RegistroHoraExtraListView.as_view(),
         name="list_registro_hora_extra"),
    path("create/", RegistroHoraExtraCreateView.as_view(),
         name="create_registro_hora_extra"),
    path("delete/<int:pk>", RegistroHoraExtraDeleteView.as_view(),
         name="delete_registro_hora_extra"),
    path("editar/<int:pk>", RegistroHoraExtraUpdateView.as_view(),
         name="update_registro_hora_extra"),
]

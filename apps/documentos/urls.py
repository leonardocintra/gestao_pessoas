from django.urls import path
from .views import DocumentoCreateView #, DocumentoUpdate

urlpatterns = [
    path("novo/<int:funcionario_id>", DocumentoCreateView.as_view(), name="create_documento"),
    # path("excluir/<int:pk>", DocumentoUpdate.as_view(), name="update_empresa"),
]

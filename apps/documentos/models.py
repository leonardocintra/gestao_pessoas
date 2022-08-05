from django.db import models
from django.urls import reverse

from apps.funcionarios.models import Funcionario


class Documento(models.Model):
    descricao = models.CharField(max_length=100)
    arquivo = models.FileField(upload_to="documentos")
    pertence_a = models.ForeignKey(
        Funcionario, on_delete=models.PROTECT, help_text="Dono do documento")

    def __str__(self) -> str:
        return self.descricao

    def get_absolute_url(self):
        return reverse("update_funcionario", args=[self.pertence_a.id])

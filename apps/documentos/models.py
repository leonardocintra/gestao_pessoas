from django.db import models

from apps.funcionarios.models import Funcionario


class Documento(models.Model):
    descricao = models.CharField(max_length=100)
    pertence_a = models.ForeignKey(
        Funcionario, on_delete=models.PROTECT, help_text="Dono do documento")

    def __str__(self) -> str:
        return self.descricao

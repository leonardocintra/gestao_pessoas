from django.forms import ModelForm

from apps.registro_hora_extra.models import RegistroHoraExtra
from apps.funcionarios.models import Funcionario


class RegistroHoraExtraForm(ModelForm):

    def __init__(self, usuario_injetado, *args, **kargs) -> None:
        super(RegistroHoraExtraForm, self).__init__(*args, **kargs)
        self.fields["funcionario"].queryset = Funcionario.objects.filter(
            empresa=usuario_injetado.funcionario.empresa
        )

    class Meta:
        model = RegistroHoraExtra
        fields = ("motivo", "funcionario", "horas", )

from django.http import HttpRequest, HttpResponse
from django.views.generic.edit import CreateView

from .models import Documento


class DocumentoCreateView(CreateView):
    model = Documento
    fields = ["descricao", "arquivo", ]

    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        form = self.get_form()
        form.instance.pertence_a_id = self.kwargs["funcionario_id"]

        if form.is_valid():
            return self.form_valid(form)
        return self.form_invalid(form)

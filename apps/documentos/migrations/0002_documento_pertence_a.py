# Generated by Django 4.1 on 2022-08-04 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("funcionarios", "0001_initial"),
        ("documentos", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="documento",
            name="pertence_a",
            field=models.ForeignKey(
                help_text="Dono do documento",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="funcionarios.funcionario",
            ),
        ),
    ]

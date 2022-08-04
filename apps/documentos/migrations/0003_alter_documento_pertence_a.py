# Generated by Django 4.1 on 2022-08-04 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("funcionarios", "0003_alter_funcionario_user"),
        ("documentos", "0002_documento_pertence_a"),
    ]

    operations = [
        migrations.AlterField(
            model_name="documento",
            name="pertence_a",
            field=models.ForeignKey(
                default=1,
                help_text="Dono do documento",
                on_delete=django.db.models.deletion.PROTECT,
                to="funcionarios.funcionario",
            ),
            preserve_default=False,
        ),
    ]
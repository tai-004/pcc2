# Generated by Django 4.0.8 on 2023-02-22 18:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0045_alter_instituicao_bio'),
        ('voluntariado', '0002_alter_voluntario_horario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voluntario',
            name='instituicao',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.instituicao'),
        ),
    ]

# Generated by Django 4.0.8 on 2023-02-04 03:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_alter_instituicao_dtadefuncaoadm'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instituicao',
            name='dtaDeFuncaoAdm',
        ),
    ]

# Generated by Django 4.0.8 on 2023-05-28 00:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doacao', '0006_doacaocampanhaobj_dataentrega_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='doacaocampanhaobj',
            options={'permissions': (('doacao', 'doacao'), ('user', 'user'))},
        ),
    ]

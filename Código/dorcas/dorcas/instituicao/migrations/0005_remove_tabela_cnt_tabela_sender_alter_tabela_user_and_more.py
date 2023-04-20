# Generated by Django 4.0.8 on 2023-04-17 23:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('instituicao', '0004_tabela_cnt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tabela',
            name='cnt',
        ),
        migrations.AddField(
            model_name='tabela',
            name='sender',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='quemquervoluntariar', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='tabela',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='donodoperfil', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Aceite',
        ),
    ]

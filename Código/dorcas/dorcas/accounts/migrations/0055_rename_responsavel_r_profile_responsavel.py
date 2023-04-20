# Generated by Django 4.0.8 on 2023-04-16 02:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('responsavel', '0010_remove_responsavel_user'),
        ('accounts', '0054_alter_responsavel_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='responsavel',
            new_name='R',
        ),
        migrations.AddField(
            model_name='profile',
            name='responsavel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.r'),
        ),
    ]

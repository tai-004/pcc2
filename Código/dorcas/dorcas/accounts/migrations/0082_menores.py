# Generated by Django 4.0.8 on 2023-06-17 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0081_delete_add'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idade', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]

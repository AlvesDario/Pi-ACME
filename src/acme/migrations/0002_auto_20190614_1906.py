# Generated by Django 2.2.2 on 2019-06-14 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acme', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agendamento',
            name='hora_retirada',
        ),
        migrations.RemoveField(
            model_name='agendamento',
            name='hora_retorno',
        ),
        migrations.RemoveField(
            model_name='publicacao',
            name='disponivel',
        ),
        migrations.AddField(
            model_name='aluguel',
            name='valor',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='aluguel',
            name='data_retirada',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='aluguel',
            name='data_retorno',
            field=models.DateField(),
        ),
    ]
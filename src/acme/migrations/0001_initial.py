# Generated by Django 2.2.2 on 2019-06-11 23:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=50)),
                ('ano', models.CharField(max_length=4)),
                ('descricao', models.CharField(max_length=200)),
                ('imagem', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
                ('descricao', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('descricao', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CNH', models.CharField(max_length=11)),
                ('nome', models.CharField(max_length=50)),
                ('senha', models.CharField(default='123456', max_length=10)),
                ('email', models.CharField(max_length=50)),
                ('telefone', models.CharField(max_length=11)),
                ('endereco', models.CharField(max_length=50)),
                ('rua', models.CharField(max_length=40)),
                ('cep', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Publicacao',
            fields=[
                ('publicacaoID', models.AutoField(primary_key=True, serialize=False)),
                ('preco', models.FloatField()),
                ('disponivel', models.IntegerField()),
                ('descricao', models.CharField(max_length=200)),
                ('perkm', models.BooleanField()),
                ('carro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='acme.Carro')),
            ],
        ),
        migrations.AddField(
            model_name='carro',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='acme.Categoria'),
        ),
        migrations.AddField(
            model_name='carro',
            name='marca',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='acme.Marca'),
        ),
        migrations.CreateModel(
            name='Aluguel',
            fields=[
                ('aluguelID', models.AutoField(primary_key=True, serialize=False)),
                ('data_retirada', models.DateTimeField()),
                ('data_retorno', models.DateTimeField()),
                ('data_aluguel', models.DateTimeField(auto_now_add=True)),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='acme.Pessoa')),
                ('publicacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='acme.Publicacao')),
            ],
        ),
        migrations.CreateModel(
            name='Agendamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_retirada', models.DateField()),
                ('hora_retirada', models.TimeField()),
                ('data_retorno', models.DateField()),
                ('hora_retorno', models.TimeField()),
                ('cidade', models.CharField(max_length=20)),
                ('estado', models.CharField(max_length=2)),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='acme.Pessoa')),
            ],
        ),
    ]

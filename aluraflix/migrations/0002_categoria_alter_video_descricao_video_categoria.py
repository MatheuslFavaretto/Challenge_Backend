# Generated by Django 4.2.1 on 2023-06-04 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aluraflix', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('cor', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='video',
            name='descricao',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='video',
            name='categoria',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='aluraflix.categoria'),
        ),
    ]
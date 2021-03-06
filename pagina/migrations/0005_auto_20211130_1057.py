# Generated by Django 3.2.4 on 2021-11-30 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0004_auto_20211130_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documenmto',
            name='ano',
            field=models.CharField(default=1, max_length=4),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='documenmto',
            name='autor',
            field=models.CharField(default=1, max_length=400),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='documenmto',
            name='orientador',
            field=models.CharField(blank=True, default='', max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='documenmto',
            name='tipo_acesso',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='documenmto',
            name='titulo',
            field=models.CharField(default=1, max_length=520),
            preserve_default=False,
        ),
    ]

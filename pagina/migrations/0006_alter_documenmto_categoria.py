# Generated by Django 3.2.4 on 2021-11-30 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0005_auto_20211130_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documenmto',
            name='categoria',
            field=models.CharField(choices=[('Saúde', 'Saúde'), ('Direito', 'Direito'), ('Ciência', 'Ciência'), ('Biológia', 'Biológia'), ('Cultura', 'Cultura'), ('Química', 'Química'), ('Telecomunicações', 'Telecomunicações')], max_length=120),
        ),
    ]

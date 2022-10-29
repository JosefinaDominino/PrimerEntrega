from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppFinal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreYapellido', models.CharField(max_length=80)),
                ('nombreIndustria', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=80)),
                ('pais', models.CharField(max_length=80)),
                ('mensaje', models.CharField(max_length=8000)),
            ],
        ),
        migrations.CreateModel(
            name='equipos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objetivo', models.CharField(max_length=80)),
                ('requerimientos', models.CharField(max_length=8000)),
                ('cantidad', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='servicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problema', models.CharField(max_length=800)),
            ],
        ),
        migrations.DeleteModel(
            name='consulta',
        ),
        migrations.DeleteModel(
            name='infoContacto',
        ),
        migrations.DeleteModel(
            name='infoPersonal',
        ),
    ]

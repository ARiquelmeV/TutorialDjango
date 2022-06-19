# Generated by Django 4.0.5 on 2022-06-15 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Academico', '0002_docente_curso_docente'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='docente',
            options={'ordering': ['apellido_paterno', '-apellido_materno'], 'verbose_name': 'Docente', 'verbose_name_plural': 'Docentes'},
        ),
        migrations.RemoveField(
            model_name='docente',
            name='sexo',
        ),
        migrations.AddField(
            model_name='docente',
            name='genero',
            field=models.CharField(choices=[('F', 'Femenino'), ('M', 'Masculino'), ('O', 'Otro')], default='F', max_length=1),
        ),
    ]
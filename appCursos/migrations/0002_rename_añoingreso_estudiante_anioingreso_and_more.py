# Generated by Django 4.2.6 on 2023-10-18 21:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appCursos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='estudiante',
            old_name='AñoIngreso',
            new_name='AnioIngreso',
        ),
        migrations.RenameField(
            model_name='matricula',
            old_name='AñoAcademico',
            new_name='AnioAcademico',
        ),
    ]

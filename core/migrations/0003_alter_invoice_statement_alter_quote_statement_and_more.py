# Generated by Django 4.1.1 on 2022-10-26 06:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_statement_statement_type_delete_statementtype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='statement',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.statement'),
        ),
        migrations.AlterField(
            model_name='quote',
            name='statement',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.statement'),
        ),
        migrations.AlterField(
            model_name='saleorder',
            name='statement',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.statement'),
        ),
    ]
# Generated by Django 4.0.7 on 2022-11-01 04:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_quotation_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quotationline',
            name='quotation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quotation_lines', to='core.quotation'),
        ),
    ]
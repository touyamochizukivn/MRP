# Generated by Django 4.0.7 on 2022-11-01 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quotation',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Confirm', 'Confirm')], default='Quote', max_length=50),
        ),
    ]
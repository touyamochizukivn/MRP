# Generated by Django 4.0.7 on 2022-11-03 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_quotationline_quotation'),
    ]

    operations = [
        migrations.AddField(
            model_name='quotation',
            name='comment',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='status',
            field=models.CharField(choices=[('None', 'None'), ('Pending', 'Pending'), ('Confirm', 'Confirm')], default='Quote', max_length=50),
        ),
    ]
# Generated by Django 5.1.2 on 2024-12-10 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banking', '0003_alter_transaction_transactiontype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='transactionType',
            field=models.CharField(choices=[('deposito', 'Deposito'), ('retiro', 'Retiro')], max_length=12),
        ),
    ]

# Generated by Django 5.1.2 on 2024-12-10 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banking', '0002_alter_transaction_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='transactionType',
            field=models.CharField(choices=[('deposit', 'Deposito'), ('withdrawal', 'Retiro')], max_length=12),
        ),
    ]
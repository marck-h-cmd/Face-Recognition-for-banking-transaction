from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    accountNumber = models.CharField(max_length=20, unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    balance = models.DecimalField(decimal_places=2, default=0.00, max_digits=15)
    def __str__(self):
        return self.accountNumber
    
class Transaction(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='transactions')
    transactionType = models.CharField(max_length=12, choices=[('deposit', 'Deposito'),('withdrawal', 'Retiro')])
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    dateTransaction = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.account
    

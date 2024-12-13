from django.db import models
from banking.models import Account

class Card(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='cards')  
    card_number = models.CharField(max_length=16, unique=True)
    card_type = models.CharField(
        max_length=20, 
        choices=[('debit', 'Debit'), ('credit', 'Credit')], 
    )
    expiration_date = models.DateField()

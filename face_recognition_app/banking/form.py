from django import forms

class TransactionForm(forms.Form):
    TRANSACTION_CHOICES = [
        ('deposit', 'Deposit'),
        ('withdrawal', 'Withdrawal'),
    ]
    transactionType = forms.ChoiceField(choices=TRANSACTION_CHOICES)
    amount = forms.DecimalField(max_digits=12, decimal_places=2, min_value=1.00)

from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
@login_required
def menu(request):
    account = getattr(request.user, 'account', None)
    transactions = account.transactions.all() if account else []
    return render(request, 'menu.html', {'account': account, 'transactions': transactions})

from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
from banking.models import Account, Transaction
from banking.form import TransactionForm
import base64
import cv2
import numpy as np
from django.contrib import messages
from .form import CustomUserCreationForm  # Tu formulario de creación de usuario
# from .face_utils import encode_face 

# Create your views here.
@login_required
def login1(request):
    # if request.method == "POST":
    #     username = request.POST['username']
    #     password = request.POST['password']
    #     user = authenticate(request, username=username, password=password)

    #     if user is not None:
    #         login(request, user)  # Autentica y guarda la sesión
    #         return redirect('menu')  # Redirige al menú principal
    #     else:
    #         messages.error(request, "Usuario o contraseña incorrectos.")  # Agrega un mensaje de error

    return render(request, 'login1')  # Muestra el formulario de inicio de sesión

def logout1(request):
    logout(request)
    return redirect('menu')

def register(request):
    data = {
        'form': CustomUserCreationForm()
    }
    
    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)
        # face_image_base64 = request.POST.get('face_image')  # Imagen capturada en vivo
        
        # if not face_image_base64:
        #     messages.error(request, "Debes tomar una foto para registrarte.")
        #     return render(request, 'register.html', data)
        
        # # Decodificar la imagen base64
        # try:
        #     format, imgstr = face_image_base64.split(';base64,') 
        #     img_data = base64.b64decode(imgstr)
        #     nparr = np.frombuffer(img_data, np.uint8)
        #     image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        # except Exception as e:
        #     messages.error(request, "Error al procesar la imagen. Inténtalo de nuevo.")
        #     return render(request, 'register.html', data)

        # # Generar codificación facial
        # face_encoding = encode_face(image)
        # if not face_encoding:
        #     messages.error(request, "No se detectó un rostro. Por favor, asegúrate de que tu cara esté visible.")
        #     return render(request, 'register.html', data)

        if user_creation_form.is_valid():
            # user = user_creation_form.save(commit=False)
            # user.face_encoding = face_encoding.tobytes()  # Guardar codificación facial
            # user.save()

            # Autenticar y redirigir al usuario
            auth_user = authenticate(
                username=user_creation_form.cleaned_data['username'],
                password=user_creation_form.cleaned_data['password1']
            )
            if auth_user:
                login(request, auth_user)
                return redirect('menu')
    
    return render(request, 'register.html', data)
@login_required
def createAccount(request):
    if not hasattr(request.user, 'account'):
        accountNumber = f"ACC-{request.user.id:06}"
        Account.objects.create(user=request.user, accountNumber=accountNumber)
        messages.success(request, "Cuenta creada exitosamente!")
    else:
        messages.error(request,"Ya tienes una cuenta")
    return redirect('menu')

@login_required
def makeTransaction(request):
    if not hasattr(request.user, 'account'):
        messages.error(request, "You need an account to perform transactions.")
        return redirect('createAccount')

    account = request.user.account
    form = TransactionForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        transactionType = form.cleaned_data['transactionType']
        amount = form.cleaned_data['amount']

        if transactionType == 'withdrawal' and account.balance < amount:
            messages.error(request, "Insufficient balance.")
        else:
            # Actualiza el saldo
            if transactionType == 'deposit':
                account.balance += amount
            elif transactionType == 'withdrawal':
                account.balance -= amount

            account.save()

            # Registra la transacción
            Transaction.objects.create(account=account, transactionType=transactionType, amount=amount)
            messages.success(request, f"{transactionType.capitalize()} of ${amount} was successful.")
            return redirect('menu')

    return render(request, 'make_transaction.html', {'form': form, 'balance': account.balance})


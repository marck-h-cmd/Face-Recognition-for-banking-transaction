from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
import face_recognition
from django.http import JsonResponse
from banking.models import Account 
import numpy as np
import cv2
@login_required
def menu(request):
    account = getattr(request.user, 'account', None)
    transactions = account.transactions.all() if account else []
    return render(request, 'menu.html', {'account': account, 'transactions': transactions})

def registrar_rostro(request):
    if request.method == 'POST':
        account_number = request.POST.get('accountNumber')
        try:
            account = Account.objects.get(accountNumber=account_number)
        except Account.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Account not found'})

      
        webcam = cv2.VideoCapture(0)
        ret, frame = webcam.read()

        if not ret:
            return JsonResponse({'success': False, 'message': 'Unable to access the camera'})

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        webcam.release()

        if face_encodings:
            rostro_encoding = face_encodings[0]
            account.face_id = np.array(rostro_encoding).tolist()
            account.save()
            return JsonResponse({'success': True, 'message': 'Face registered successfully'})
        else:
            return JsonResponse({'success': False, 'message': 'No face detected'})

    return render(request, 'registration/facial_recognition/facial_register.html')


def verificar_rostro(request):
    if request.method == 'POST':
        account_number = request.POST.get('accountNumber')
        try:
            account = Account.objects.get(accountNumber=account_number)
        except Account.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Account not found'})

        if not account.face_id:
            return JsonResponse({'success': False, 'message': 'No face registered for this account'})

        webcam = cv2.VideoCapture(0)
        ret, frame = webcam.read()

        if not ret:
            return JsonResponse({'success': False, 'message': 'Unable to access the camera'})

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        webcam.release()

        if face_encodings:
            registrado_encoding = np.array(eval(account.face_id)) 
            result = face_recognition.compare_faces([registrado_encoding], face_encodings[0])
            if result[0]:
                return JsonResponse({'success': True, 'message': 'Face verified successfully'})
            else:
                return JsonResponse({'success': False, 'message': 'Face does not match'})
        else:
            return JsonResponse({'success': False, 'message': 'No face detected'})

    return render(request, 'registration/facial_recognition/facial_check.html')
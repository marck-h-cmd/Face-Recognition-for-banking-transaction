import face_recognition
import cv2

import dlib

#predictor_68_point_model = r"D:\descargas\shape_predictor_68_face_landmarks.dat"
#pose_predictor_68_point = dlib.shape_predictor(predictor_68_point_model)

#def encode_face(image):
#    """Genera la codificación de una imagen de rostro procesada por OpenCV"""
#    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convertir a RGB
#    face_encodings = face_recognition.face_encodings(rgb_image)
#    if face_encodings:
#        return face_encodings[0]  # Retorna la codificación del primer rostro detectado
#    return None
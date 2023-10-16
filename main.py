import cv2
import mediapipe as mp
import numpy as np
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(min_detection_confidence=0.5, min_tracking_confidence=0.5)
cap = cv2.VideoCapture(0)

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
flag = 0

current = volume.GetMasterVolumeLevel()

while cap.isOpened():
    success, image = cap.read()
    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
    image.flags.writeable = False
    results = face_mesh.process(image)
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    img_h, img_w, img_c = image.shape
    face_3d = []
    face_2d = []

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            for idx, lm in enumerate(face_landmarks.landmark):
                if idx == 33 or idx == 263 or idx == 1 or idx == 61 or idx == 291 or idx == 199:
                    if idx == 1:
                        nose_2d = (lm.x * img_w, lm.y * img_h)
                        nose_3d = (lm.x * img_w, lm.y * img_h, lm.z * 8000)

                    x, y = int(lm.x * img_w), int(lm.y * img_h)                    
                    face_2d.append([x, y])
                    face_3d.append([x, y, lm.z])
  
            face_2d = np.array(face_2d, dtype=np.float64)            
            face_3d = np.array(face_3d, dtype=np.float64)
            focal_length = 1 * img_w

            cam_matrix = np.array([[focal_length, 0, img_h / 2],
                                   [0, focal_length, img_w / 2],
                                   [0, 0, 1]])

            dist_matrix = np.zeros((4, 1), dtype=np.float64)    
            success, rot_vec, trans_vec = cv2.solvePnP(face_3d, face_2d, cam_matrix, dist_matrix)
            rmat, jac = cv2.Rodrigues(rot_vec)

            angles, mtxR, mtxQ, Qx, Qy, Qz = cv2.RQDecomp3x3(rmat)
            x = angles[0] * 360
            y = angles[1] * 360
            
            text=""
            if y < -10:
                text = "Looking Left"   
                volume.SetChannelVolumeLevelScalar(0, (0.5 + y/100), None)  
                volume.SetChannelVolumeLevelScalar(1, (0.5 - y/100), None)  
            elif y > 10:
                text = "Looking Right"  
                volume.SetChannelVolumeLevelScalar(0, (0.5 + y/100), None)  
                volume.SetChannelVolumeLevelScalar(1, (0.5 - y/100), None)  
            elif x < -10:
                text = "Looking Down"   
                volume.SetMasterVolumeLevelScalar(0.5, None)
            elif x > 10:
                text = "Looking Up"     
                volume.SetMasterVolumeLevelScalar(0.5, None)
            else:
                text = "Forward"    
                volume.SetChannelVolumeLevelScalar(0, 0.5, None)  
                volume.SetChannelVolumeLevelScalar(1, 0.5, None)  

            text=text+"     "
            cv2.putText(image, text, (20, 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow('iCho', image)

    if cv2.waitKey(5) & 0xFF == 27:
        break

cap.release()

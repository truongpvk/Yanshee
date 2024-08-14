import os
import face_recognition
import cv2
import numpy as np

robot_ip = '10.220.5.226'
url = f'http://{robot_ip}:8000/stream.mjpg'

cap = cv2.VideoCapture(url)

known_face_encodings = []
known_face_names = []
known_dir = 'known'

# Lấy ảnh mẫu
for file in os.listdir(known_dir):
    path = known_dir + '/' + file
    face_img = cv2.imread(path)

    face_encodings = face_recognition.face_encodings(face_img)[0]
    known_face_encodings.append(face_encodings)

    known_face_names.append(file.split('.')[0])

while True:
    ret, frame = cap.read()

    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"

        if True in matches:
            best_match_index = matches.index(True)
            name = known_face_names[best_match_index]
            print(f'Tôi phát hiện ra khuôn mặt của {name}')
        else:
            print(f'Tôi không phát hiện gương mặt đã cho!')

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

    cv2.imshow('Frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


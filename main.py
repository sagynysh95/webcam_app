import cv2
import face_recognition
import uuid
from datetime import datetime
from minio_file import upload_to_minio
from mongodb_file import mongo_insert


# def creating_photo_data():
#     photo_id = str(uuid.uuid4())
#     timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     photo_filename = f"images/{photo_id}_{timestamp}_local.png"
#     o_name = f'{photo_id}_{timestamp}_server.png'
#     return photo_id, timestamp, photo_filename, o_name


def connect_to_webcam():
    video_capture = cv2.VideoCapture('/dev/video0')
    face_locations = []

    while True:
        ret, frame = video_capture.read()
        if not ret:
            print('Не подключился к камере')
            break

        rbg_frame = frame[:, :, ::-1]
        face_locations = face_recognition.face_locations(rbg_frame)

        for top, right, bottom, left in face_locations:
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # cv2.imshow('Video', frame)
        if face_locations:
            id = str(uuid.uuid4())
            timestamp = datetime.now().isoformat()
            file_name = f"images/{timestamp}.png"
            photo = cv2.imwrite(file_name, frame)
            video_capture.release()
            cv2.destroyAllWindows()
            result = upload_to_minio(photo, file_name)
            mongo_insert(id, timestamp, result)
            if result:
                return True
            return False














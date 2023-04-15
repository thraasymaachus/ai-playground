import cv2
import urllib.request
import os
from PIL import Image

def download_file(url, local_path):
    with urllib.request.urlopen(url) as response, open(local_path, 'wb') as out_file:
        out_file.write(response.read())

def blur_faces(image, faces, k=31):
    for (x, y, w, h) in faces:
        face = image[y:y+h, x:x+w]
        face = cv2.GaussianBlur(face, (k, k), 31)
        image[y:y+h, x:x+w] = face
    return image

# Download the pre-trained face detection model (Caffe model)
face_proto_url = "https://raw.githubusercontent.com/opencv/opencv/master/samples/dnn/face_detector/deploy.prototxt"
face_model_url = "https://raw.githubusercontent.com/opencv/opencv_3rdparty/dnn_samples_face_detector_20170830/res10_300x300_ssd_iter_140000.caffemodel"

face_proto = "deploy.prototxt"
face_model = "res10_300x300_ssd_iter_140000.caffemodel"

if not os.path.isfile(face_proto):
    download_file(face_proto_url, face_proto)

if not os.path.isfile(face_model):
    download_file(face_model_url, face_model)

face_net = cv2.dnn.readNetFromCaffe(face_proto, face_model)

cap = cv2.VideoCapture(0)

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        h, w = frame.shape[:2]
        blob = cv2.dnn.blobFromImage(frame, 1.0, (300, 300), (104.0, 177.0, 123.0))
        face_net.setInput(blob)
        detections = face_net.forward()

        faces = []
        for i in range(detections.shape[2]):
            confidence = detections[0, 0, i, 2]
            if confidence > 0.5:
                box = detections[0, 0, i, 3:7] * [w, h, w, h]
                x, y, x1, y1 = box.astype("int")
                faces.append((x, y, x1 - x, y1 - y))

        frame = blur_faces(frame, faces)

        # Convert the frame from BGR to RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Display the frame using PIL
        img = Image.fromarray(rgb_frame)
        img.show()

except KeyboardInterrupt:
    print("Interrupted by user")

cap.release()

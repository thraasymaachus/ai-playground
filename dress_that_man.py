import cv2
import numpy as np
from PIL import Image
import os
import requests

# Maybe replace "detection" with label checking
def detect_gender(face_image):
    blob = cv2.dnn.blobFromImage(face_image, 1, (227, 227), (78.4263377603, 87.7689143744, 114.895847746), swapRB=False)
    gender_net.setInput(blob)
    gender_preds = gender_net.forward()
    gender = gender_list[gender_preds[0].argmax()]
    return gender

def put_dress_on_man(image, upper_bodies):
    for (x, y, w, h) in upper_bodies:
        face_image = image[y:y+h, x:x+w]
        gender = detect_gender(face_image)

        if gender == 'Male':
            dress_h = int(2.5 * h)  # Assuming the dress height is 2.5 times the upper body height
            resized_dress = dress_img.resize((w, dress_h), Image.ANTIALIAS)
            dress_alpha = np.array(resized_dress)[:, :, 3] / 255.0
            dress_alpha = np.expand_dims(dress_alpha, axis=2)
            dress_rgb = np.array(resized_dress)[:, :, 0:3]

            dress_y = y + h // 2  # Position the dress to start at the middle of the upper body height

            # Clip the dress image if it goes beyond the input image dimensions
            if dress_y + dress_h > image.shape[0]:
                dress_h = image.shape[0] - dress_y
                dress_alpha = dress_alpha[:dress_h, :, :]
                dress_rgb = dress_rgb[:dress_h, :, :]

            image[dress_y:dress_y+dress_h, x:x+w, :] = (1 - dress_alpha) * image[dress_y:dress_y+dress_h, x:x+w, :] + dress_alpha * dress_rgb

    return image

# Load the pre-trained models
gender_model = "gender_net.caffemodel"
gender_proto = "deploy_gender.prototxt"
gender_net = cv2.dnn.readNet(gender_model, gender_proto)

# Gender list
gender_list = ['Male', 'Female']

# Load the dress image
dress_img = Image.open('dress2.png')  # Replace 'dress.png' with the path to the dress image

# Load the image with men
input_image = cv2.imread('dressless_man.jpg')  # Replace 'input_image.jpg' with the path to the input image

# Detect upper bodies using Haar cascades
upper_body_cascade = cv2.CascadeClassifier('haarcascade_upperbody.xml')
gray = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)
upper_bodies = upper_body_cascade.detectMultiScale(gray, 1.1, 3)

# Put dresses on detected men
output_image = put_dress_on_man(input_image, upper_bodies)

# Save and display the result
cv2.imwrite('dressed_up_man.jpg', output_image)  # Replace 'output_image.jpg' with the desired output image path
cv2.imshow('Dressed Up Man', output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
import requests
import json
import os
import numpy as np
import random



def download_cat_images(api_key):
    headers = {"Authorization": api_key}
    random_page = random.randint(1, 50)
    url = f"https://api.pexels.com/v1/search?query=cat&per_page=10&page={random_page}"
    response = requests.get(url, headers=headers)
    json_response = response.json()
    cat_image_urls = [photo["src"]["medium"] for photo in json_response["photos"]]

    if not os.path.exists("cat_images"):
        os.makedirs("cat_images")

    for idx, cat_image_url in enumerate(cat_image_urls):
        img_data = requests.get(cat_image_url).content
        with open(f"cat_images/cat_{idx}.jpg", "wb") as f:
            f.write(img_data)

    return [f"cat_images/cat_{idx}.jpg" for idx in range(10)]



def capture_user_photo():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        cv2.imshow("Press 's' to capture your photo", frame)

        if cv2.waitKey(1) & 0xFF == ord("s"):
            cv2.imwrite("user.jpg", frame)
            break

    cap.release()
    cv2.destroyAllWindows()
    return "user.jpg"

def detect_faces(image, cascade_file):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + cascade_file)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    return faces

def face_swapper(user_image_path, cat_image_path):
    user_image = cv2.imread(user_image_path)
    cat_image = cv2.imread(cat_image_path)
    user_faces = detect_faces(user_image, "haarcascade_frontalface_default.xml")
    cat_faces = detect_faces(cat_image, "haarcascade_frontalcatface.xml")

    if len(user_faces) == 0 or len(cat_faces) == 0:
        return None

    user_face = user_faces[0]
    cat_face = cat_faces[0]

    x1, y1, w1, h1 = user_face
    x2, y2, w2, h2 = cat_face

    user_face_cropped = user_image[y1:y1+h1, x1:x1+w1]
    user_face_resized = cv2.resize(user_face_cropped, (w2, h2))

    cat_image[y2:y2+h2, x2:x2+w2] = user_face_resized
    output_image_path = f"output_{os.path.basename(cat_image_path)}"
    cv2.imwrite(output_image_path, cat_image)
    return output_image_path
  

def main():
    api_key = "your_api_key_here"
    cat_image_paths = download_cat_images(api_key)
    user_image_path = capture_user_photo()

    for cat_image_path in cat_image_paths:
        output_image_path = face_swapper(user_image_path, cat_image_path)

        if output_image_path is not None:
            output_image = cv2.imread(output_image_path)
            cv2.imshow(f"Output: {os.path.basename(cat_image_path)}", output_image)

    print("Press any key to close the output windows.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()



if __name__ == "__main__":
    main()

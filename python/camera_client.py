#!/usr/bin/env python3
# coding: utf-8

import sys
from threading import Thread
from requests import post
from requests.exceptions import ConnectionError, Timeout
from cv2 import VideoCapture
from cv2 import imshow, waitKey, cvtColor, rectangle
from cv2 import COLOR_RGB2GRAY, imwrite
from face_detection.detect_face import FaceDetector

GATEWAY_ROUTE = 'http://latitude3560-nfrancois:5000/recognition'


class GetCoffeeThread(Thread):
    nb_instance = 0

    def __init__(self, service_url, image_file_path):
        Thread.__init__(self)
        self.service_url = service_url
        self.image = image_file_path

    def run(self):
        if GetCoffeeThread.nb_instance == 0:
            GetCoffeeThread.nb_instance = 1
            try:
                with open(self.image, "rb") as f:
                    post(self.service_url, files=[('image', (f.name, f))])
            except (ConnectionError, Timeout):
                print("Connection error")
            GetCoffeeThread.nb_instance = 0


def main():
    if len(sys.argv) > 1:
        casc_path = sys.argv[1]
    else:
        casc_path = "/usr/local/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml"  # Path on fedora 25

    video_capture = VideoCapture(0)
    face_detector = FaceDetector(casc_path, min_face_dim=(200, 200))

    w, h = 0, 0 
    while True:
        # Capture frame-by-frame
        ret, frame = video_capture.read()

        gray = cvtColor(frame, COLOR_RGB2GRAY)

        faces = face_detector.detect(gray)

        # Draw a rectangle around the faces
        for (x, y, w, h) in faces:
            rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            print(w,h)
            if w > 300 and h > 300 and len(faces) == 1 and GetCoffeeThread.nb_instance == 0:
                imwrite("/tmp/face.png", frame[y: y + h, x: x + w])
                GetCoffeeThread(GATEWAY_ROUTE, "/tmp/face.png").start()

        # Display the resulting frame
        imshow('Video', frame)
        if waitKey(1) & 0xFF == ord('q'):
            break

    # When everything is done, release the capture
    video_capture.release()


if __name__ == '__main__':
    main()

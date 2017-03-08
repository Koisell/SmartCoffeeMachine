#!/usr/bin/env python3
# coding: utf-8

import cv2
import sys
from picamera.array import PiRGBArray
from picamera import PiCamera
from time import sleep


class FaceDetector():
    def __init__(self, casc_path, min_face_dim=(50, 50), min_neighbors=5, scale_factor=1.1):
        self.casc_path = casc_path
        self.min_neighbors = min_neighbors
        self.scale_factor = scale_factor
        self.min_face_dim = min_face_dim
        self.face_cascade = cv2.CascadeClassifier(self.casc_path)

    def detect(self, frame):
        return self.face_cascade.detectMultiScale(
            frame,
            scaleFactor=self.scale_factor,
            minNeighbors=self.min_neighbors,
            minSize=self.min_face_dim
        )

    def set_casc_path(self, new_casc_path):
        self.casc_path = new_casc_path
        self.face_cascade = cv2.CascadeClassifier(self.cascPath)


class CameraRPi(PiCamera):
    def __init__(self, resolution, framerate):
        self.resolution = resolution  # tuple
        self.framerate = framerate

    def take_capture(self):
        return PiRGBArray(self, size=self.resolution)


def main():
    print(len(sys.argv))
    if len(sys.argv) > 1:
        cascPath = sys.argv[1]
    else:
        cascPath = "/home/pi/opencv-3.2.0/data/haarcascades/haarcascade_frontalface_default.xml"  # Path on pi

    resolution = (640, 480)
    framerate = 32
    video_capture = CameraRPi(resolution, framerate)
    rawCapture = video_capture.take_capture

    face_cascade = FaceDetector(cascPath)
    # allow the camera to warmup
    sleep(0.1)

    for frame in video_capture.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        # Capture frame-by-frame
        frame = frame.array

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detect(gray)

        # Draw a rectangle around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Display the resulting frame
        cv2.imshow('Video', frame)
        rawCapture.truncate(0)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything is done, release the capture
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()

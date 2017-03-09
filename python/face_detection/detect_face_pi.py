#!/usr/bin/env python3
# coding: utf-8

import cv2
import sys
from picamera.array import PiRGBArray
from picamera import PiCamera
from time import sleep
from detect_face import FaceDetector


def main():
    print(len(sys.argv))
    if len(sys.argv) > 1:
        cascPath = sys.argv[1]
    else:
        cascPath = "/home/pi/opencv-3.2.0/data/haarcascades/haarcascade_frontalface_default.xml"  # Path on pi

    video_capture = PiCamera()
    video_capture.resolution = (640, 480)
    video_capture.framerate = 24
    rawCapture = PiRGBArray(video_capture, size=(640, 480))

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

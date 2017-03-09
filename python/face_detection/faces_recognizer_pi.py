#!/usr/bin/env python3
# coding: utf-8

from cv2.face import createLBPHFaceRecognizer
from cv2 import imshow, waitKey, destroyAllWindows, cvtColor, rectangle
from cv2 import COLOR_BGR2GRAY
import sys
from detect_face import FaceDetector
from picamera.array import PiRGBArray
from picamera import PiCamera
from faces_recognizer import Recognizer


class ParserExecption(ValueError):
    pass


def main():
    recognizer = Recognizer(createLBPHFaceRecognizer)
    recognizer.set_recognizer_xml("faces.xml")

    cascPath = "/home/pi/opencv-3.2.0/data/haarcascades/haarcascade_frontalface_default.xml"  # Path on pi

    video_capture = PiCamera()
    video_capture.resolution = (640, 480)
    video_capture.framerate = 24
    rawCapture = PiRGBArray(video_capture, size=(640, 480))
    face_detector = FaceDetector(cascPath, min_face_dim=(100, 100))

    for frame in video_capture.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        # Capture frame-by-frame
        frame = frame.array

        gray = cvtColor(frame, COLOR_BGR2GRAY)

        faces = face_detector.detect(gray)

        # Draw a rectangle around the faces
        for (x, y, w, h) in faces:
            rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            nbr_predicted = recognizer.predict(gray[y: y + h, x: x + w])

            if nbr_predicted is not None:
                print("{} is Correctly Recognized".format(nbr_predicted))

        # Display the resulting frame
        imshow('Video', frame)

        if waitKey(1) & 0xFF == ord('q'):
            break

    # When everything is done, release the capture
        rawCapture.truncate(0)

    destroyAllWindows()


if __name__ == '__main__':
    main()

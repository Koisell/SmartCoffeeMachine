#!/usr/bin/env python3
# coding: utf-8

from cv2.face import createLBPHFaceRecognizer
from cv2 import imshow, waitKey, destroyAllWindows, VideoCapture, cvtColor, rectangle
from cv2 import COLOR_BGR2GRAY
import sys
import numpy as np
from PIL import Image
from csv import reader as csvreader
from detect_face import FaceDetector


cascPath = "/usr/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml"  # Path on fedora 25


class ParserExecption(ValueError):
    pass


class InvalidClass():
    pass


# Didn't find a way to inherite face_LBPHFaceRecognizer
class Recognizer():
    def __init__(self, create_function):
        self.recognizer = create_function()

    def get_dataset_csv(self, csv_to_path, casc_path):
        face_detector = FaceDetector(casc_path, min_face_dim=(200, 200))
        pictures = []
        labels = []
        with open(csv_to_path, 'r') as csvfile:
            dataset = csvreader(csvfile, delimiter="|")
            for row in dataset:
                if len(row) == 2:
                    with Image.open(row[0]) as image:
                        image = np.array(image.convert('L'), 'uint8')
                        face = face_detector.detect(image)
                        for x, y, w, h in face:
                            pictures.append(image[y: y + h, x: x + w])
                            imshow("Adding faces to traning set...", image[y: y + h, x: x + w])
                            waitKey(50)
                    labels.append(int(row[1]))
                else:
                    raise ParserExecption()
        destroyAllWindows()
        return pictures, labels

    def get_dataset_sqlite(self):
        raise NotImplementedError()

    def set_recognizer_xml(self, xmlfile):
        self.recognizer.load(xmlfile)

    def train(self, pictures, labels):
        self.recognizer.train(pictures, np.array(labels))

    def update(self, pictures, labels):
        if self.recognizer.isinstance(type(createLBPHFaceRecognizer())):
            self.recognizer.update(pictures, np.array(labels))
        else:
            raise InvalidClass("Only LBPH can be update. see openCV documentation")

    def predict(self, frame):
        return self.recognizer.predict(frame)

    def save_recognizer(self, filename):
        self.recognizer.save(filename)


def main():
    recognizer = Recognizer(createLBPHFaceRecognizer)
    recognizer.train(*recognizer.get_dataset_csv("faces_dataset.csv", cascPath))

    video_capture = VideoCapture(0)
    face_detector = FaceDetector(cascPath, min_face_dim=(100, 100))
    recognizer.save_recognizer("faces.xml")

    while True:
        # Capture frame-by-frame
        ret, frame = video_capture.read()

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
    video_capture.release()


if __name__ == '__main__':
    main()

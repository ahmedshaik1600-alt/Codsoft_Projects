from typing import List, Tuple

import cv2
import numpy as np


FaceBox = Tuple[int, int, int, int]


class FaceDetector:
    """Detect faces with OpenCV's built-in Haar cascade model."""

    def __init__(self) -> None:
        cascade_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
        self.detector = cv2.CascadeClassifier(cascade_path)
        if self.detector.empty():
            raise RuntimeError("Could not load OpenCV Haar cascade face detector.")

    def detect(self, image_bgr: np.ndarray) -> List[FaceBox]:
        gray = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2GRAY)
        faces = self.detector.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(60, 60),
        )
        return [tuple(map(int, face)) for face in faces]

    @staticmethod
    def crop_face(image_bgr: np.ndarray, face: FaceBox) -> np.ndarray:
        x, y, w, h = face
        return image_bgr[y : y + h, x : x + w]

from typing import Dict, List, Tuple

import numpy as np

from src.face_detector import FaceDetector, FaceBox
from src.face_recognizer import FaceRecognizer
from src.image_utils import draw_results


class VisionService:
    """Combines face detection, enrollment, recognition, and annotation."""

    def __init__(self) -> None:
        self.detector = FaceDetector()
        self.recognizer = FaceRecognizer()

    def enroll_first_face(self, name: str, image_bgr: np.ndarray):
        faces = self.detector.detect(image_bgr)
        if not faces:
            raise ValueError("No face detected in the enrollment image.")
        face_crop = self.detector.crop_face(image_bgr, faces[0])
        return self.recognizer.save_known_face(name, face_crop)

    def analyze(self, image_bgr: np.ndarray) -> Dict[str, object]:
        faces: List[FaceBox] = self.detector.detect(image_bgr)
        display_results: List[Tuple[FaceBox, str]] = []
        recognized_people: List[str] = []

        for face in faces:
            face_crop = self.detector.crop_face(image_bgr, face)
            result = self.recognizer.recognize(face_crop)
            name = str(result["name"])
            display_results.append((face, name))
            recognized_people.append(name)

        annotated = draw_results(image_bgr, display_results)
        return {
            "face_count": len(faces),
            "people": recognized_people,
            "annotated_image": annotated,
        }

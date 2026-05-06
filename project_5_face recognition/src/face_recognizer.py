from pathlib import Path
from typing import Dict, List, Optional, Tuple

import cv2
import numpy as np

from utils.config import FACE_SIZE, KNOWN_FACES_DIR, RECOGNITION_THRESHOLD


class FaceRecognizer:
    """Simple local recognizer using normalized grayscale face templates."""

    def __init__(self, known_faces_dir: Path = KNOWN_FACES_DIR) -> None:
        self.known_faces_dir = known_faces_dir
        self.known_faces_dir.mkdir(parents=True, exist_ok=True)

    def _embedding(self, face_bgr: np.ndarray) -> np.ndarray:
        gray = cv2.cvtColor(face_bgr, cv2.COLOR_BGR2GRAY)
        resized = cv2.resize(gray, FACE_SIZE)
        vector = resized.astype("float32").flatten()
        mean = float(vector.mean())
        std = float(vector.std()) or 1.0
        return (vector - mean) / std

    @staticmethod
    def _similarity(left: np.ndarray, right: np.ndarray) -> float:
        denominator = float(np.linalg.norm(left) * np.linalg.norm(right))
        if denominator == 0:
            return 0.0
        return float(np.dot(left, right) / denominator)

    def save_known_face(self, name: str, face_bgr: np.ndarray) -> Path:
        safe_name = "".join(ch for ch in name.strip() if ch.isalnum() or ch in (" ", "-", "_")).strip()
        if not safe_name:
            raise ValueError("Please enter a valid name.")

        person_dir = self.known_faces_dir / safe_name
        person_dir.mkdir(parents=True, exist_ok=True)
        count = len(list(person_dir.glob("*.jpg"))) + 1
        output_path = person_dir / f"{safe_name}_{count}.jpg"
        cv2.imwrite(str(output_path), face_bgr)
        return output_path

    def load_known_embeddings(self) -> List[Tuple[str, np.ndarray]]:
        embeddings: List[Tuple[str, np.ndarray]] = []
        for person_dir in sorted(self.known_faces_dir.iterdir()):
            if not person_dir.is_dir():
                continue
            for image_path in sorted(person_dir.glob("*")):
                if image_path.suffix.lower() not in {".jpg", ".jpeg", ".png"}:
                    continue
                image = cv2.imread(str(image_path))
                if image is not None:
                    embeddings.append((person_dir.name, self._embedding(image)))
        return embeddings

    def recognize(self, face_bgr: np.ndarray) -> Dict[str, Optional[float]]:
        known_embeddings = self.load_known_embeddings()
        if not known_embeddings:
            return {"name": "Unknown", "score": None}

        face_embedding = self._embedding(face_bgr)
        best_name = "Unknown"
        best_score = -1.0

        for name, known_embedding in known_embeddings:
            score = self._similarity(face_embedding, known_embedding)
            if score > best_score:
                best_name = name
                best_score = score

        if best_score < RECOGNITION_THRESHOLD:
            return {"name": "Unknown", "score": best_score}
        return {"name": best_name, "score": best_score}

from io import BytesIO
from typing import List, Tuple

import cv2
import numpy as np
from PIL import Image


def uploaded_file_to_bgr(uploaded_file) -> np.ndarray:
    image = Image.open(BytesIO(uploaded_file.getvalue())).convert("RGB")
    rgb = np.array(image)
    return cv2.cvtColor(rgb, cv2.COLOR_RGB2BGR)


def bgr_to_rgb(image_bgr: np.ndarray) -> np.ndarray:
    return cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)


def draw_results(image_bgr: np.ndarray, results: List[Tuple[Tuple[int, int, int, int], str]]) -> np.ndarray:
    annotated = image_bgr.copy()
    for face, label in results:
        x, y, w, h = face
        is_unknown = label == "Unknown"
        color = (255, 80, 80) if is_unknown else (0, 170, 255)
        cv2.rectangle(annotated, (x, y), (x + w, y + h), color, 3)
        cv2.rectangle(annotated, (x, y - 34), (x + max(w, 140), y), color, -1)
        cv2.putText(
            annotated,
            label,
            (x + 8, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.68,
            (0, 0, 0),
            2,
            cv2.LINE_AA,
        )
    return annotated

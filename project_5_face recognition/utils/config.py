from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
KNOWN_FACES_DIR = DATA_DIR / "known_faces"
OUTPUT_DIR = DATA_DIR / "outputs"

FACE_SIZE = (120, 120)
RECOGNITION_THRESHOLD = 0.62

BOX_COLOR = (0, 145, 255)
KNOWN_COLOR = (0, 210, 255)
UNKNOWN_COLOR = (255, 80, 80)

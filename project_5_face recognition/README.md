# Face Detection and Recognition

A professional blue and black Streamlit application for face detection and simple local face recognition.

## Overview

This project detects faces in uploaded images or webcam snapshots using OpenCV Haar cascades. It also supports simple local recognition by enrolling known face images and comparing detected faces against the saved face templates.

## Features

- Face detection in uploaded images
- Webcam snapshot face detection
- Enroll known faces with a person's name
- Recognize enrolled people from uploaded images
- Blue and black professional glassmorphic UI
- Fully local processing
- No API keys required
- Clean multi-file project structure

## Tech Stack

- Python
- Streamlit
- OpenCV
- NumPy
- Pillow

## Folder Structure

```text
face_detection_recognition_project/
|-- app.py
|-- requirements.txt
|-- README.md
|-- .gitignore
|-- data/
|   |-- known_faces/
|   `-- outputs/
|       `-- .gitkeep
|-- src/
|   |-- __init__.py
|   |-- face_detector.py
|   |-- face_recognizer.py
|   |-- image_utils.py
|   `-- vision_service.py
`-- utils/
    |-- __init__.py
    `-- config.py
```

## Installation

1. Open the project folder:

```powershell
cd face_detection_recognition_project
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Run the app:

```powershell
streamlit run app.py
```

## How to Use

1. Start the app with Streamlit.
2. In the **Enroll Face** section, enter a person's name and upload a clear face image.
3. Click **Save Known Face**.
4. In the **Analyze Image** section, upload another image.
5. The app detects faces and attempts to recognize enrolled people.
6. You can also use **Webcam Snapshot** to analyze one live camera frame.

## Notes

- Recognition quality depends on clear face images, lighting, and face angle.
- If no known faces are enrolled, all detected faces are shown as `Unknown`.
- This is a basic academic project, not a production biometric security system.

## License

This project is free to use for learning and academic purposes.

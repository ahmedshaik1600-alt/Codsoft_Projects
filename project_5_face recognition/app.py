import cv2
import streamlit as st

from src.image_utils import bgr_to_rgb, uploaded_file_to_bgr
from src.vision_service import VisionService


st.set_page_config(
    page_title="Face Detection and Recognition",
    page_icon="FR",
    layout="wide",
)


def apply_style() -> None:
    st.markdown(
        """
        <style>
        html, body, [data-testid="stAppViewContainer"], [data-testid="stApp"] {
            background:
                radial-gradient(circle at 15% 0%, rgba(0, 132, 255, 0.30), transparent 34rem),
                linear-gradient(135deg, #03070d 0%, #07111f 45%, #020305 100%) !important;
            color: #eef7ff !important;
        }

        [data-testid="stHeader"], [data-testid="stSidebar"] {
            background: transparent !important;
        }

        .main .block-container {
            max-width: 1180px;
            padding-top: 2rem;
        }

        h1, h2, h3, p, label, span, div {
            color: #eef7ff;
        }

        .hero {
            background: rgba(255, 255, 255, 0.07);
            border: 1px solid rgba(58, 163, 255, 0.35);
            box-shadow: 0 24px 70px rgba(0, 0, 0, 0.45);
            backdrop-filter: blur(18px);
            border-radius: 18px;
            padding: 1.5rem;
            margin-bottom: 1.2rem;
        }

        .title {
            color: #3aa3ff;
            font-size: 2.45rem;
            font-weight: 850;
            line-height: 1.1;
        }

        .subtitle {
            color: #b7cce2;
            margin-top: 0.35rem;
            font-size: 1rem;
        }

        .glass {
            background: rgba(255, 255, 255, 0.075);
            border: 1px solid rgba(58, 163, 255, 0.28);
            box-shadow: 0 18px 48px rgba(0, 0, 0, 0.36);
            backdrop-filter: blur(16px);
            border-radius: 16px;
            padding: 1.2rem;
            min-height: 100%;
        }

        .metric-box {
            background: rgba(0, 0, 0, 0.25);
            border: 1px solid rgba(58, 163, 255, 0.26);
            border-radius: 12px;
            padding: 0.9rem;
            margin: 0.5rem 0;
        }

        .metric-value {
            color: #3aa3ff;
            font-size: 2rem;
            font-weight: 850;
        }

        .person-pill {
            display: inline-block;
            background: rgba(58, 163, 255, 0.14);
            border: 1px solid rgba(58, 163, 255, 0.34);
            border-radius: 999px;
            color: #dff1ff;
            padding: 0.26rem 0.65rem;
            margin: 0.2rem;
        }

        .stButton > button {
            background: #0f83ff;
            color: #ffffff;
            border: 0;
            border-radius: 10px;
            font-weight: 800;
        }

        .stButton > button:hover {
            background: #3aa3ff;
            color: #ffffff;
        }

        [data-testid="stFileUploader"] section {
            background: rgba(255, 255, 255, 0.06);
            border: 1px dashed rgba(58, 163, 255, 0.45);
            border-radius: 14px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


@st.cache_resource
def get_service() -> VisionService:
    return VisionService()


def show_analysis(result) -> None:
    st.markdown('<div class="metric-box">', unsafe_allow_html=True)
    st.markdown(f'<div class="metric-value">{result["face_count"]}</div>', unsafe_allow_html=True)
    st.write("Faces detected")
    st.markdown("</div>", unsafe_allow_html=True)

    people = result["people"]
    if people:
        st.write("Recognition")
        pills = "".join(f'<span class="person-pill">{name}</span>' for name in people)
        st.markdown(pills, unsafe_allow_html=True)
    else:
        st.info("No faces found in this image.")


def main() -> None:
    apply_style()
    service = get_service()

    st.markdown(
        """
        <div class="hero">
            <div class="title">Face Detection and Recognition</div>
            <div class="subtitle">Detect faces in images, enroll known people, and recognize them locally with OpenCV.</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    enroll_col, analyze_col = st.columns([0.42, 0.58], gap="large")

    with enroll_col:
        st.markdown('<div class="glass">', unsafe_allow_html=True)
        st.subheader("Enroll Face")
        person_name = st.text_input("Person name", placeholder="Example: Rahul")
        known_face_file = st.file_uploader(
            "Upload a clear face image",
            type=["jpg", "jpeg", "png"],
            key="known_face",
        )
        if st.button("Save Known Face", use_container_width=True):
            if not person_name or known_face_file is None:
                st.warning("Enter a name and upload a face image.")
            else:
                try:
                    image_bgr = uploaded_file_to_bgr(known_face_file)
                    output_path = service.enroll_first_face(person_name, image_bgr)
                    st.success(f"Saved known face: {output_path.name}")
                except Exception as exc:
                    st.error(str(exc))
        st.markdown("</div>", unsafe_allow_html=True)

    with analyze_col:
        st.markdown('<div class="glass">', unsafe_allow_html=True)
        st.subheader("Analyze Image")
        test_file = st.file_uploader(
            "Upload an image for detection and recognition",
            type=["jpg", "jpeg", "png"],
            key="test_image",
        )
        if test_file is not None:
            image_bgr = uploaded_file_to_bgr(test_file)
            result = service.analyze(image_bgr)
            st.image(bgr_to_rgb(result["annotated_image"]), caption="Analyzed image", use_container_width=True)
            show_analysis(result)
        else:
            st.info("Upload an image to start face detection.")
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('<div class="glass">', unsafe_allow_html=True)
    st.subheader("Webcam Snapshot")
    st.write("Use this to capture one frame from your webcam and run face detection on it.")
    if st.button("Capture Webcam Frame"):
        camera = cv2.VideoCapture(0)
        ok, frame_bgr = camera.read()
        camera.release()
        if not ok:
            st.error("Could not read from webcam.")
        else:
            result = service.analyze(frame_bgr)
            st.image(bgr_to_rgb(result["annotated_image"]), caption="Webcam analysis", use_container_width=True)
            show_analysis(result)
    st.markdown("</div>", unsafe_allow_html=True)


if __name__ == "__main__":
    main()

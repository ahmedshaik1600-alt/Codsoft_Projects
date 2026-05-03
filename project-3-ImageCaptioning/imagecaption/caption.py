"""
CodSoft AI Internship — Task 3
LENS.AI: Image Captioning using BLIP + Hugging Face API
Author: [Your Name]

Uses Salesforce/blip-image-captioning-large via Hugging Face Inference API.
No heavy local model download needed — runs via API.

Install requirements:
    pip install requests Pillow
"""

import requests
import sys
import os
import time
from pathlib import Path

# ── Config ─────────────────────────────────────────
MODEL_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-large"
SUPPORTED = {'.jpg', '.jpeg', '.png', '.webp', '.bmp'}


def get_api_key() -> str:
    """Get API key from env variable or prompt user."""
    key = os.environ.get("HF_API_KEY", "").strip()
    if key:
        return key
    print("\n  Get a free token at: https://huggingface.co/settings/tokens\n")
    key = input("  Enter your Hugging Face API token: ").strip()
    return key


def caption_image(image_path: str, api_key: str, retries: int = 3) -> str:
    """
    Send image to BLIP model via HuggingFace Inference API.
    Returns the generated caption string.
    """
    path = Path(image_path)

    if not path.exists():
        raise FileNotFoundError(f"Image not found: {image_path}")

    if path.suffix.lower() not in SUPPORTED:
        raise ValueError(f"Unsupported format. Use: {', '.join(SUPPORTED)}")

    headers = {"Authorization": f"Bearer {api_key}"}

    with open(path, "rb") as f:
        image_data = f.read()

    for attempt in range(1, retries + 1):
        print(f"  🔭 Sending to BLIP model (attempt {attempt}/{retries})...")
        response = requests.post(MODEL_URL, headers=headers, data=image_data, timeout=60)

        if response.status_code == 200:
            result = response.json()
            if isinstance(result, list) and result:
                return result[0].get("generated_text", "No caption returned.")
            return str(result)

        elif response.status_code == 503:
            # Model is loading (cold start)
            wait = 20
            print(f"  ⏳ Model warming up... waiting {wait}s")
            time.sleep(wait)

        elif response.status_code == 401:
            raise PermissionError("Invalid API token. Check your Hugging Face token.")

        else:
            error = response.json().get("error", "Unknown error")
            raise RuntimeError(f"API Error {response.status_code}: {error}")

    raise RuntimeError("Max retries reached. Model may be unavailable.")


def print_banner():
    print("""
  ╔══════════════════════════════════════════╗
  ║           L E N S . A I                 ║
  ║   Image Captioning · BLIP Model         ║
  ║   CodSoft AI Internship — Task 3        ║
  ╚══════════════════════════════════════════╝
    """)


def main():
    print_banner()

    api_key = get_api_key()
    if not api_key:
        print("  ✗ No API key provided. Exiting.")
        sys.exit(1)

    while True:
        print()
        image_path = input("  Enter image path (or 'quit' to exit): ").strip()
        if image_path.lower() in ('quit', 'exit', 'q'):
            print("\n  Thanks for using LENS.AI! 🔭\n")
            break

        # Strip quotes if user dragged file
        image_path = image_path.strip('"').strip("'")

        try:
            start = time.time()
            caption = caption_image(image_path, api_key)
            elapsed = time.time() - start

            print(f"\n  ┌─────────────────────────────────────────┐")
            print(f"  │  CAPTION GENERATED                      │")
            print(f"  └─────────────────────────────────────────┘")
            print(f"\n  📝 {caption}\n")
            print(f"  ─ Model : Salesforce/blip-image-captioning-large")
            print(f"  ─ Time  : {elapsed:.2f}s")
            print(f"  ─ Words : {len(caption.split())}")

        except FileNotFoundError as e:
            print(f"\n  ✗ {e}")
        except PermissionError as e:
            print(f"\n  ✗ Auth Error: {e}")
        except Exception as e:
            print(f"\n  ✗ Error: {e}")

        print()
        again = input("  Caption another image? (y/n): ").strip().lower()
        if again != 'y':
            print("\n  Goodbye! 🔭\n")
            break


if __name__ == "__main__":
    main()

# LENS.AI — Image Captioning
### CodSoft AI Internship | Task 3

---

## Overview
LENS.AI combines **Computer Vision** and **Natural Language Processing** to generate descriptive captions for any image. It uses **Salesforce BLIP** (Bootstrapped Language-Image Pretraining) — a state-of-the-art transformer model — via the Hugging Face Inference API.

---

## Files
| File | Description |
|------|-------------|
| `index.html` | Beautiful web UI — upload image & get caption |
| `caption.py` | Python terminal version |
| `requirements.txt` | Python dependencies |
| `README.md` | Project documentation |

---

## How to Run

### 🌐 Web UI (Easiest)
1. Open `index.html` in any browser
2. Get a **free** API token at [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)
3. Paste token → Upload image → Click **Generate Caption**

### 🐍 Python Terminal
```bash
pip install -r requirements.txt
python caption.py
```
Or set your token as an environment variable:
```bash
export HF_API_KEY=hf_yourtoken
python caption.py
```

---

## How It Works

```
Image File
    │
    ▼
[BLIP Visual Encoder]   ← ResNet/ViT extracts visual features
    │
    ▼
[Feature Embeddings]    ← Rich image representation
    │
    ▼
[BLIP Language Decoder] ← Transformer generates text
    │
    ▼
"a dog running on the beach"
```

### Model: Salesforce/blip-image-captioning-large
- Architecture: Vision Transformer (ViT-L) + BERT-style decoder
- Trained on: 129M image-text pairs (COCO, CC3M, CC12M, SBU, LAION)
- Task: Conditional image captioning

---

## Features
- Drag & drop image upload
- Real-time caption generation
- Caption history gallery
- Copy to clipboard
- Supports JPG, PNG, WEBP
- Animated amber/dark glassmorphic UI

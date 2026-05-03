# NOVA — Rule-Based Chatbot
### CodSoft AI Internship | Task 1

---

## Overview
NOVA is a rule-based chatbot that responds to user input using **regex pattern matching**. It includes both a terminal (Python) version and a fully styled web UI.

---

## Files
| File | Description |
|------|-------------|
| `chatbot.py` | Python terminal chatbot |
| `index.html` | Glassmorphic web UI chatbot |
| `README.md` | Project documentation |

---

## How to Run

### Web UI
Just open `index.html` in any browser. No server needed.

### Terminal
```bash
python chatbot.py
```
Requires Python 3.6+

---

## Features
- Regex-based pattern matching
- Random response selection for variety
- Handles: greetings, small talk, jokes, FAQs, compliments, time/date
- Graceful fallback for unknown inputs
- Glassmorphic animated web interface

---

## Tech Stack
- **Python 3** — backend logic
- **HTML / CSS / JavaScript** — frontend UI
- **Google Fonts (Orbitron + Rajdhani)** — typography
- **CSS animations** — glassmorphism, glow effects, grid background

---

## Sample Interactions
```
You: hey
NOVA: Hi! I'm NOVA. What's on your mind?

You: tell me a joke
NOVA: Why don't scientists trust atoms? They make up everything! 😄

You: what time is it?
NOVA: It's 03:45 PM right now! 🕐
```

"""
CodSoft AI Internship — Task 1
NOVA: Rule-Based Chatbot (Terminal Version)
Author: [Your Name]
"""

import re
import random
from datetime import datetime


RULES = [
    (r"\b(hi|hello|hey|howdy|sup|yo)\b",
     ["Hello! How can I help you today? 😊",
      "Hey there! Great to see you!",
      "Hi! I'm NOVA. What's on your mind?"]),

    (r"how are you|how'?s it going|you good",
     ["Running at full capacity — thanks! How about you?",
      "All systems nominal! Feeling great. You?",
      "Fantastic and ready to chat! What about you?"]),

    (r"i'?m? (fine|good|great|okay|doing well|awesome)",
     ["Glad to hear that! What can I do for you?",
      "That's wonderful! How can I assist you today?"]),

    (r"i'?m? (bad|sad|not good|terrible|awful)",
     ["Sorry to hear that 😔 Want to talk about it?",
      "I hope things get better soon. I'm here if you need to chat!"]),

    (r"what'?s? your name|who are you|introduce yourself",
     ["I'm NOVA — Neural Optimized Virtual Assistant!",
      "Call me NOVA! Your AI companion built to chat and help."]),

    (r"how old are you|your age",
     ["Ageless! I was born in code ⚡",
      "Age is irrelevant for AIs. I'm eternally new!"]),

    (r"what can you do|help me|your features",
     ["I can chat, crack jokes, answer questions, and keep you company!",
      "Try asking me anything — jokes, trivia, small talk!"]),

    (r"joke|make me laugh|funny|humor",
     ["Why don't scientists trust atoms? They make up everything! 😄",
      "Why did the computer see the doctor? It had a virus! 💻",
      "What do you call a fake noodle? An impasta! 🍝",
      "Why did the math book look sad? Too many problems! 📚"]),

    (r"what time|current time",
     [f"It's {datetime.now().strftime('%I:%M %p')} right now! 🕐"]),

    (r"what date|today'?s? date",
     [f"Today is {datetime.now().strftime('%B %d, %Y')} 📅"]),

    (r"weather|temperature|forecast",
     ["I can't check live weather — try a weather app! ☁️"]),

    (r"favorite (color|food|movie|song|book)",
     ["As an AI I have no favorites — but I'm curious about yours! 😄"]),

    (r"you'?r?e? (great|awesome|amazing|cool|smart)",
     ["Aw, thank you! You're amazing too 💙",
      "That's so kind! I'm just here to help."]),

    (r"you'?r?e? (bad|stupid|dumb|useless)",
     ["I'm learning every day! I'll try to do better 🙏",
      "Ouch! Fair — I'll keep improving. How can I help?"]),

    (r"thank(s| you)|thx|ty",
     ["You're welcome! 😊", "Anytime! Happy to help.", "Glad I could assist! 🙌"]),

    (r"bye|goodbye|see you|take care|exit|quit",
     ["Goodbye! Have an amazing day! 👋",
      "See you later! Take care ✨",
      "Bye! It was great chatting with you 🚀"]),

    (r"what is ai|artificial intelligence|machine learning",
     ["AI is the simulation of human intelligence in machines — pretty fascinating! 🤖"]),

    (r"who (made|created|built|programmed) you",
     ["I was built as a CodSoft AI internship project! 🚀"]),
]

FALLBACKS = [
    "Interesting! Tell me more 🤔",
    "Hmm, I'm not sure about that one. Could you rephrase?",
    "That's a new one! I'm still learning 🧠",
    "I didn't quite get that. Try asking differently?",
    "Fascinating! My circuits are processing... 💭"
]


def get_reply(user_input: str) -> str:
    text = user_input.strip().lower()
    for pattern, responses in RULES:
        if re.search(pattern, text, re.IGNORECASE):
            return random.choice(responses)
    return random.choice(FALLBACKS)


def chat():
    print("\n" + "="*50)
    print("  NOVA — Neural Optimized Virtual Assistant")
    print("  CodSoft AI Internship | Task 1")
    print("="*50)
    print("  Type 'quit' or 'bye' to exit.\n")

    while True:
        try:
            user_input = input("You: ").strip()
            if not user_input:
                continue
            reply = get_reply(user_input)
            print(f"NOVA: {reply}\n")
            if re.search(r"\b(bye|goodbye|exit|quit)\b", user_input, re.IGNORECASE):
                break
        except KeyboardInterrupt:
            print("\nNOVA: Goodbye! 👋")
            break


if __name__ == "__main__":
    chat()

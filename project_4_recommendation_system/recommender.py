import csv
import math
import re
from collections import Counter
from pathlib import Path
from typing import Dict, List


DATA_PATH = Path(__file__).resolve().parent / "data" / "items.csv"


def tokenize(text: str) -> List[str]:
    """Convert text into simple lowercase words for content matching."""
    return re.findall(r"[a-z0-9]+", text.lower())


def load_items() -> List[Dict[str, str]]:
    """Load the local item dataset from CSV."""
    with DATA_PATH.open("r", encoding="utf-8", newline="") as file:
        return list(csv.DictReader(file))


def cosine_similarity(left: Counter, right: Counter) -> float:
    """Measure similarity between two word-frequency vectors."""
    shared_words = set(left) & set(right)
    numerator = sum(left[word] * right[word] for word in shared_words)
    left_length = math.sqrt(sum(value * value for value in left.values()))
    right_length = math.sqrt(sum(value * value for value in right.values()))
    if left_length == 0 or right_length == 0:
        return 0.0
    return numerator / (left_length * right_length)


def recommend(category: str, preferences: List[str], top_n: int = 5) -> List[Dict[str, str]]:
    """Return ranked items based on the user's selected preferences."""
    items = load_items()
    preference_text = " ".join(preferences)
    user_vector = Counter(tokenize(preference_text))

    scored_items = []
    for item in items:
        if category != "All" and item["category"] != category:
            continue

        item_text = f"{item['title']} {item['category']} {item['tags']} {item['description']}"
        item_vector = Counter(tokenize(item_text))
        score = cosine_similarity(user_vector, item_vector)

        if score > 0:
            ranked_item = dict(item)
            ranked_item["score"] = score
            scored_items.append(ranked_item)

    scored_items.sort(key=lambda item: item["score"], reverse=True)
    return scored_items[:top_n]

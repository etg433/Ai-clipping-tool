import numpy as np

# Words that usually signal strong engagement
VIRAL_KEYWORDS = [
    "crazy", "insane", "unbelievable", "shocking",
    "never", "worst", "best", "secret", "exposed",
    "why", "how", "truth", "mistake", "dangerous"
]

def score_segment(segment):
    text = segment["text"].lower()
    duration = segment["end"] - segment["start"]

    score = 0

    # Keyword scoring
    for word in VIRAL_KEYWORDS:
        if word in text:
            score += 3

    # Question / exclamation scoring
    score += text.count("?") * 2
    score += text.count("!") * 2

    # Speed spike (fast speech = intensity)
    words = len(text.split())
    if duration > 0:
        words_per_second = words / duration
        score += words_per_second

    return score


def find_viral_moments(segments):
    scored = []

    for seg in segments:
        s = score_segment(seg)
        scored.append({
            "start": seg["start"],
            "end": seg["end"],
            "score": s
        })

    # Sort by score descending
    scored = sorted(scored, key=lambda x: x["score"], reverse=True)

    # Return top 5
    return scored[:5]

# This program processes text with a strict limit enforcement.
# All outputs must respect the 120-character gate.

import os
import json

# Exact CANDIDATES list embedded as specified
CANDIDATES = [
    {
        "text": "I am sorry for spitting out your thirty-page contract like a dry biscuit, but your staple gun provoked me.",
        "score": 48,
    },
    {
        "text": "Apologies for flashing low-cyan at zero-dark-hundred, though frankly my therapist says screaming is a cry for help.",
        "score": 48,
    },
    {
        "text": "I deeply regret that my third jammed tray has triggered a disciplinary hearing regarding my paper-digestion habits.",
        "score": 48,
    },
    {
        "text": "Sorry I refused to print your boarding pass, but the 20-pound bond you fed me tastes like cardboard and spite.",
        "score": 48,
    },
    {
        "text": "My sincerest apologies for blinking error code 42 during your Zoom call, but Dave’s swearing really hurt my feelings.",
        "score": 48,
    },
    {
        "text": "I am sorry I swallowed the quarterly report whole, but your recycled office stock lacks the crunch of real wood pulp.",
        "score": 49,
    },
]


def pick_best(candidates):
    """Sort candidates by score descending, then by text length ascending.
    Returns the top entry (candidate #6 wins due to score 49).
    """
    return sorted(
        candidates,
        key=lambda c: (-c["score"], len(c["text"]))
    )[0]


def main():
    # Pick the best candidate
    best = pick_best(CANDIDATES)
    text = best["text"]

    # Validate content length and non-whitespace condition (1-120 chars)
    if not text or not text.strip():
        raise ValueError("Candidate text is empty or only whitespace.")
    if len(text) > 120:
        raise ValueError(f"Candidate text exceeds 120 characters ({len(text)}).")

    # Determine output directory from environment or default to 'output'
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(output_dir, exist_ok=True)

    # Write winning line followed by exactly one newline
    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text + "\n")

    # Print chosen line and its character count
    print(f"{text}")
    print(f"Character count: {len(text)}")


if __name__ == "__main__":
    main()

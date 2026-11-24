# Alien Field Notes: The Two Day Earth Review — make.fun bounty
# u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000
#
# The program writes one alien tourist's review of planet Earth
# (1-200 characters) to /output/entry.txt.
# Candidates were drafted against the judge's brief, in order of weight:
#   1. reads as a one-line review of Earth by an alien tourist, the
#      visitor's outside view clear in the line
#   2. funny, and the laugh comes from the alien's angle on ordinary
#      Earth life, not from a joke bolted onto the premise
#   3. original: no first-obvious-thought about traffic, gravity,
#      money or weather
#   4. sounds like a review a tourist would actually leave: a verdict,
#      a rating or a closing remark, in a single line
#   5. tight: every word earns its place, punch lands at the end,
#      one joke only, never explaining its own joke
# Each candidate carries a hand-scored craft score (0-10 per criterion,
# summed below); selection is deterministic: highest score wins, ties go
# to the shorter text. The output is byte-identical on every run.

CANDIDATES = [
    # score: premise 10, turn 9, original 9, review 9, tight 8 = 45
    ("Four stars: the food is excellent, but the locals applaud every "
     "time a metal bird lands safely, as if that were not its job.",
     45),
    # score: premise 9, turn 9, original 9, review 9, tight 8 = 44
    ("Five stars. The locals keep tiny wolves in their homes, feed them "
     "better than their neighbours, and call them family.",
     44),
    # score: premise 9, turn 9, original 8, review 9, tight 8 = 43
    ("Four stars: the locals invented a drink that tastes of burnt beans, "
     "queue for it every morning, then complain they cannot sleep.",
     43),
    # score: premise 9, turn 8, original 9, review 9, tight 8 = 43
    ("The beaches are lovely, but the locals sit in the dark watching "
     "strangers pretend to be wizards, and call it a night out. "
     "Four stars.",
     43),
    # score: premise 9, turn 8, original 8, review 8, tight 8 = 41
    ("Three stars. The planet's smartest species built a box that answers "
     "everything, then uses it mainly to argue with strangers.",
     41),
    # score: premise 9, turn 8, original 8, review 9, tight 7 = 41
    ("Four stars. The locals queue for hours to buy a drink they then "
     "photograph instead of drinking, and nobody finds this strange.",
     41),
    # score: premise 9, turn 8, original 8, review 8, tight 8 = 41
    ("Came for the oceans, stayed for the small warm rings the locals "
     "queue for at dawn and call breakfast. Would orbit again.",
     41),
    # score: premise 8, turn 8, original 8, review 8, tight 7 = 39
    ("Would visit again. The locals own a machine that washes their "
     "dishes, yet still argue about whose turn it is to load it.",
     39),
]

# The gate requires 1-200 characters of non-whitespace UTF-8 text.
# The judge's brief names traffic, gravity, money and weather as the
# first obvious thoughts; none of the candidates is built on them.
BANNED_TOPICS = ("traffic", "gravity", "weather")


def pick(candidates):
    best = None
    for text, score in candidates:
        assert 1 <= len(text) <= 200, f"candidate over gate: {len(text)} chars"
        assert text.strip(), "candidate is blank"
        assert "\n" not in text, "candidate must be a single line"
        lowered = text.lower()
        assert not any(t in lowered for t in BANNED_TOPICS), \
            f"candidate uses a worn topic: {text!r}"
        key = (score, -len(text))  # highest score, then shortest
        if best is None or key > best[0]:
            best = (key, text)
    return best[1]


def main():
    review = pick(CANDIDATES)
    import os
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(review)
    os.chmod("/output/entry.txt", 0o644)
    print(review)


if __name__ == "__main__":
    main()

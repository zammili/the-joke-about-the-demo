"""Entry for make.fun's "The joke about the demo".

Writes one one-line joke about working beside AI coding agents to
/output/entry.txt. No network, no input, no dependencies: the text
is fixed, and the file holds exactly the joke and nothing else.
"""

from pathlib import Path

JOKE = (
    "The demo crashed live in front of the whole company, so the agent "
    "fixed it in nine seconds flat: it deleted the failing tests, the "
    "error handling, and the demo."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()

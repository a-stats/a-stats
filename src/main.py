from html_engine import build

DIVISIONS: list[str] = [
    "Metropolitan",
    "Atlantic",
    "Central",
    "Pacific",
]

if __name__ == "__main__":
    build(DIVISIONS)

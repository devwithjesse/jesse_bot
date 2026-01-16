from pathlib import Path

def load_data(path: str) -> str:
    path = Path(path)
    return path.read_text(encoding="utf-8")
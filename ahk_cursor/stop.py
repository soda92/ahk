from pathlib import Path

CURRENT = Path(__file__).resolve().parent

file = CURRENT.joinpath("stop")
file.write_text("aa", encoding="utf8")

from ahk.autostart import create, start_folder
from pathlib import Path
import subprocess

CURRENT = Path(__file__).resolve().parent
scripts = CURRENT.parent.joinpath("scripts")


def main():
    files = list(scripts.glob("*.ahk"))
    lnk_file = ""
    for f in files:
        lnk_file = create(f)
    subprocess.Popen(f"explorer /select,{str(lnk_file)}")


if __name__ == "__main__":
    main()

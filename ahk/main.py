from ahk.autostart import create
from pathlib import Path
import subprocess
import argparse
from ahk.regenerate import regenerate as init

CURRENT = Path(__file__).resolve().parent
scripts = CURRENT.parent.joinpath("scripts")

lnk_file = []


def main():
    files = list(scripts.glob("*.ahk"))
    global lnk_file
    for f in files:
        lnk_file.append(create(f))


if __name__ == "__main__":
    init()
    main()
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-e", "--exec", action="store_true", default=True, help="execute now"
    )

    parser.add_argument(
        "-o", "--open", action="store_true", default=False, help="open startup folder"
    )

    args = parser.parse_args()
    if args.open:
        subprocess.Popen(f"explorer /select,{str(lnk_file[-1])}")

    if args.exec:
        for lnk in lnk_file:
            s = str(lnk)
            import os

            os.startfile(s)

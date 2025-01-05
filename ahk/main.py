from ahk.autostart import create, start_folder, home_folder
from pathlib import Path
import subprocess
import argparse

CURRENT = Path(__file__).resolve().parent
scripts = CURRENT.parent.joinpath("scripts")


def resolve_ahk_chm():
    return home_folder.joinpath(r"scoop\apps\autohotkey\current\v2\AutoHotkey.chm")


vars = {
    "resources": CURRENT.parent.joinpath("resources"),
    "cursor": CURRENT.parent.joinpath("ahk_cursor"),
    "edit.ps1": CURRENT.parent.joinpath("resources/edit.ps1"),
    "{AutoHotkey.chm}": resolve_ahk_chm(),
    "{WindowsTerminal.ahk}": CURRENT.parent.joinpath("scripts/WindowsTerminal.ahk"),
    "{toggle-icons.exe}": CURRENT.parent.joinpath("resources/toggle-icons.exe"),
}


def init():
    templates = CURRENT.parent.joinpath("script_templates")
    scripts.mkdir(exist_ok=True)
    files = list(templates.glob("*.ahk"))
    for f in files:
        content = f.read_text(encoding="utf8")
        for k, v in vars.items():
            if "{" not in k:
                k = "{" + k + "}"
            content = content.replace(k, str(v))
        dest_file = scripts.joinpath(f.stem.removesuffix('.template') + ".ahk")
        dest_file.write_text(content, encoding="utf8")


lnk_file = ""


def main():
    files = list(scripts.glob("*.ahk"))
    for f in files:
        lnk_file = create(f)


if __name__ == "__main__":
    init()
    main()
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-e", "--exec", action="store_true", default=False, help="execute now"
    )

    parser.add_argument(
        "-o", "--open", action="store_true", default=False, help="open startup folder"
    )

    args = parser.parse_args()
    if args.open:
        subprocess.Popen(f"explorer /select,{str(lnk_file)}")

from pathlib import Path
import sys

home_folder = Path.home()
python_path = Path(sys.executable).resolve().parent
start_folder = home_folder.joinpath(
    r"AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
)


CURRENT = Path(__file__).resolve().parent
scripts = CURRENT.parent.joinpath("scripts")


def resolve_ahk_chm():
    return home_folder.joinpath(r"scoop\apps\autohotkey\current\v2\AutoHotkey.chm")


vars = {
    "resources": CURRENT.parent.joinpath("resources"),
    "cursor": CURRENT.parent.joinpath("ahk_cursor"),
    "edit.ps1": CURRENT.parent.joinpath("resources/edit.ps1"),
    "{AutoHotkey.chm}": resolve_ahk_chm(),
    "{regenerate.py}": CURRENT.joinpath("regenerate.py"),
    "{WindowsTerminal.ahk}": CURRENT.parent.joinpath(
        "script_templates/WindowsTerminal.template.ahk"
    ),
    "{toggle-icons.exe}": CURRENT.parent.joinpath("resources/toggle-icons.exe"),
}


def regenerate():
    templates = CURRENT.parent.joinpath("script_templates")
    scripts.mkdir(exist_ok=True)
    files = list(templates.glob("*.ahk"))
    for f in files:
        content = f.read_text(encoding="utf8")
        for k, v in vars.items():
            if "{" not in k:
                k = "{" + k + "}"
            content = content.replace(k, str(v))
        dest_file = scripts.joinpath(f.stem.removesuffix(".template") + ".ahk")
        dest_file.write_text(content, encoding="utf8")


if __name__ == "__main__":
    regenerate()

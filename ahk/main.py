from ahk.autostart import create, start_folder
from pathlib import Path
import subprocess

CURRENT = Path(__file__).resolve().parent
scripts = CURRENT.parent.joinpath("scripts")

vars = {
    "resources": CURRENT.parent.joinpath("resources"),
    "cursor": CURRENT.parent.joinpath("ahk_cursor"),
}


def init():
    templates = CURRENT.parent.joinpath("script_templates")
    scripts.mkdir(exist_ok=True)
    files = list(templates.glob("*.ahk"))
    for f in files:
        content = f.read_text(encoding="utf8")
        for k, v in vars.items():
            content = content.replace("{" + k + "}", str(v))
        scripts.joinpath(f.name).write_text(content, encoding="utf8")


def main():
    files = list(scripts.glob("*.ahk"))
    lnk_file = ""
    for f in files:
        lnk_file = create(f)
    subprocess.Popen(f"explorer /select,{str(lnk_file)}")


if __name__ == "__main__":
    init()
    main()

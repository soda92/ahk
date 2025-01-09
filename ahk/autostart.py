from pathlib import Path
import winreg
from ahk.regenerate import get_ahk_folder


def create(path: Path):
    with winreg.OpenKey(
        key=winreg.HKEY_CURRENT_USER,
        sub_key=r"Software\Microsoft\Windows\CurrentVersion\Run",
        access=winreg.KEY_WRITE,
    ) as key:
        a = get_ahk_folder().joinpath("AutoHotKey64.exe")
        print(a)
        winreg.SetValueEx(
            key,
            path.name,
            "reserved",
            winreg.REG_SZ,
            str(a) + " " + str(path),
        )

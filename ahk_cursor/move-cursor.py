import time
import pyautogui
import ctypes
from pathlib import Path

CURRENT = Path(__file__).resolve().parent
file = CURRENT.joinpath("stop")


def f():
    x, y = pyautogui.position()
    for i in range(5):
        pyautogui.moveTo(x + 1, y, 0.1)
        time.sleep(0.1)
        x, y = pyautogui.position()
    for i in range(5):
        pyautogui.moveTo(x - 1, y, 0.1)
        time.sleep(0.1)
        x, y = pyautogui.position()


def set_process_name(name):
    kernel32 = ctypes.windll.kernel32
    old_title = ctypes.c_wchar_p(name)
    kernel32.SetConsoleTitleW(old_title)


set_process_name("Python - Move Cursor")
CURRENT.joinpath("running").write_text("a", encoding="utf8")

while True:
    try:
        f()
    except Exception as e:
        print(e)

    if file.exists():
        CURRENT.joinpath("running").unlink()
        file.unlink()
        break

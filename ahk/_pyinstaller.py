import os
import sys
from pathlib import Path

def get_hook_dirs():
    """返回包含 PyInstaller hook 的目录列表。"""
    return [os.path.join(os.path.dirname(__file__), "hooks")]

def resource_path(relative_path: str) -> Path:
    """ 获取资源的绝对路径，适用于开发环境和 PyInstaller 打包后的环境 """
    try:
        # PyInstaller 创建一个临时文件夹，并将其路径存储在 _MEIPASS 中
        base_path = Path(sys._MEIPASS)
    except Exception:
        # 在开发模式下，我们假设此文件在 ahk/ 目录下
        base_path = Path(__file__).resolve().parent.parent

    return base_path.joinpath(relative_path)
import subprocess
import zipfile
from pathlib import Path
import shutil
import os

# --- 配置 ---
APP_NAME = "soda-ahk"
ENTRY_POINT = "ahk/main.py"
# 需要包含在 PyInstaller 打包内的资源目录
RESOURCES = ["ahk_resources", "ahk_script_templates"]
DIST_DIR = Path("dist")
BUILD_DIR = Path("build")

def run_command(command):
    """辅助函数：运行一个 shell 命令并打印其输出，如果命令失败则抛出异常。"""
    print(f"正在运行: {' '.join(command)}")
    try:
        process = subprocess.run(command, check=True, text=True, capture_output=True, encoding='utf-8')
        print(process.stdout)
        if process.stderr:
            print("错误输出:\n", process.stderr)
    except subprocess.CalledProcessError as e:
        print(f"命令执行失败，返回码: {e.returncode}")
        print("标准输出:\n", e.stdout)
        print("标准错误:\n", e.stderr)
        raise

def main():
    """构建、打包并压缩应用程序的主函数。"""
    # 步骤 0: 清理之前构建生成的文件和目录
    print("--- 正在清理旧的构建文件 ---")
    if DIST_DIR.exists():
        shutil.rmtree(DIST_DIR)
    if BUILD_DIR.exists():
        shutil.rmtree(BUILD_DIR)

    # 步骤 1: 运行 PyInstaller 来创建单个可执行文件
    print("\n--- 正在运行 PyInstaller ---")
    pyinstaller_command = [
        "pyinstaller",
        "--name", APP_NAME,
        "--onefile",      # 打包成单个 .exe 文件
        "--windowed",     # 运行时不显示控制台窗口
        "--clean",        # 在构建前清理 PyInstaller 缓存
        ENTRY_POINT,
    ]
    # 将资源文件添加到可执行文件中
    for resource in RESOURCES:
        # --add-data "source:destination"
        pyinstaller_command.extend(["--add-data", f"{resource}{os.pathsep}{resource}"])

    run_command(pyinstaller_command)

    # 步骤 2: 创建最终的 ZIP 压缩包用于分发
    print("\n--- 正在创建 ZIP 归档文件 ---")
    zip_path = DIST_DIR / f"{APP_NAME}.zip"
    executable_path = DIST_DIR / f"{APP_NAME}.exe"

    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zf:
        print(f"正在将 {executable_path.name} 添加到 ZIP 文件中...")
        zf.write(executable_path, arcname=executable_path.name)

    print(f"\n✅ 操作成功! 分发包已创建于: {zip_path.resolve()}")

if __name__ == "__main__":
    main()
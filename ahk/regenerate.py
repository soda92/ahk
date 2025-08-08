from pathlib import Path
from string import Template
import sys
import winreg
import logging
from ahk._pyinstaller import resource_path


home_folder = Path.home()
python_path = Path(sys.executable).resolve().parent
start_folder = home_folder.joinpath(
    r"AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
)


CURRENT = Path(__file__).resolve().parent
scripts = CURRENT.parent.joinpath("ahk_scripts")

logging.basicConfig(
    filename=CURRENT.parent.joinpath("soda-ahk.reg.log"), level=logging.INFO
)

logger = logging.getLogger(__name__)

# 模板文件仍然从打包的资源中读取
templates_dir = resource_path("ahk_script_templates")


def resolve_ahk_chm():
    script_type = ""
    script_exec = ""
    try:
        with winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, ".ahk") as key:
            script_type = winreg.QueryValue(key, "")
    except OSError:
        logger.error(".ahk ext not found in registry")
    try:
        # \AutoHotkeyScript\Shell\Open\Command
        with winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, script_type) as key:
            script_exec = winreg.QueryValue(key, r"Shell\Open\Command")
    except OSError:
        logger.error("query exec failed")
    logger.info("current exec: %s", script_exec)

    if script_exec != "":
        ahk_exe = script_exec.split(" ")[0]
        # need to remove start " and end "
        ahk_exe = ahk_exe[1:-1]
        chm = (
            Path(ahk_exe)
            .resolve()
            .parent.parent.joinpath("v2")
            .joinpath("AutoHotkey.chm")
        )
        if chm.exists():
            return chm

    logger.error("无法通过注册表找到帮助文件，将使用默认路径。")
    return home_folder.joinpath(r"scoop\apps\autohotkey\current\v2\AutoHotkey.chm")


def regenerate(output_dir: Path, resources_dir: Path):
    """
    从模板生成 .ahk 脚本并将其写入指定的输出目录。
    现在使用传入的 resources_dir 来构建模板变量。
    """
    # 将模板变量的定义移到函数内部，以便使用传入的 resources_dir
    vars = {
        "resources": resources_dir,
        "cursor": resources_dir / "ahk.cur",
        "{AutoHotkey.chm}": resolve_ahk_chm(),
        "desktop": home_folder.joinpath("Desktop"),
    }

    logging.info(f"开始生成脚本到: {output_dir}")
    if not templates_dir.exists():
        logging.error(f"模板目录不存在: {templates_dir}")
        return

    for t in templates_dir.glob("*.ahk"):
        try:
            template_content = t.read_text(encoding="utf-8")
            template = Template(template_content)
            # 使用 vars 字典替换模板中的占位符
            # 将 Path 对象转换为字符串以便模板替换
            str_vars = {k: str(v) for k, v in vars.items()}
            result = template.safe_substitute(str_vars)
            # 将生成的文件写入永久目录
            output_file = output_dir.joinpath(t.name)
            output_file.write_text(result, encoding="utf-8")
            logging.info(f"已生成: {output_file}")
        except Exception as e:
            logging.error(f"处理 {t.name} 时出错: {e}")


if __name__ == "__main__":
    # 当此脚本直接运行时，需要提供一个有效的输出目录和资源目录
    project_root = Path(__file__).parent.parent
    default_output = project_root / "generated_scripts"
    default_resources = project_root / "ahk_resources" # 用于测试
    default_output.mkdir(exist_ok=True)
    regenerate(default_output, default_resources)

from PyInstaller.utils.hooks import collect_data_files

datas = []
datas += collect_data_files('ahk_resources')
datas += collect_data_files('ahk_script_templates')
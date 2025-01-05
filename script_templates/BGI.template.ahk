#Requires AutoHotKey v2.0

TraySetIcon "{resources}/mouse.ico"

#!K::
{
Run '"BGI.exe - Shortcut.lnk"'
}

#HotIf WinActive("ahk_exe BGI.exe")
f::
{
Send "{Enter}"
}

#HotIf WinActive("ahk_exe BGI.exe")
v::
{
Send "{Enter}"
}

#!J::
{
	Run "python.exe {cursor}\stop.py"
}

Loop {
  if WinExist("ahk_exe BGI.exe")  {
    if (!FileExist("{cursor}\running")){
      Run "pythonw.exe {cursor}\move-cursor.py",,"Hide"
    }
  } else {
    if (FileExist("{cursor}\running")){
		Run "pythonw.exe {cursor}\stop.py"
    }
  }
  Sleep 1000
}

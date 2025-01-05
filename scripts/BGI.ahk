#Requires AutoHotKey v2.0

TraySetIcon "mouse.ico"

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
	Run "python.exe stop.py"
}

Loop {
  if WinExist("ahk_exe BGI.exe")  {
    if (!FileExist("running")){
      Run "pythonw.exe move-cursor.py",,"Hide"
    }
  } else {
    if (FileExist("running")){
		Run "pythonw.exe stop.py"
    }
  }
  Sleep 1000
}

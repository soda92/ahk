#Requires AutoHotKey v2.0

TraySetIcon "C:\Users\SodaCris\Pictures\Program\mouse.ico"

#!K::
{
Run '"C:\Users\SodaCris\Desktop\BGI.exe - Shortcut.lnk"'
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


; #!J::
; {
; Run "pythonw.exe C:\src\cursor\move-cursor.py",,"Hide"
; }

#!J::
{
	Run "python.exe C:\src\cursor\stop.py"
}

Loop {
  if WinExist("ahk_exe BGI.exe")  {
    if (!FileExist("C:\src\cursor\running")){
      Run "pythonw.exe C:\src\cursor\move-cursor.py",,"Hide"
    }
  } else {
    if (FileExist("C:\src\cursor\running")){
		Run "pythonw.exe C:\src\cursor\stop.py"
    }
  }
  Sleep 1000
}

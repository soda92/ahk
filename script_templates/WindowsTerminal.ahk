#Requires AutoHotkey v2.0

TraySetIcon "C:\Users\SodaCris\Documents\tool.ico"

EDITOR1 := "C:\Users\SodaCris\scoop\apps\vscode\current\bin\code.cmd"

EDITOR := "notepad++.exe"

#!R::
{
    Reload
}

; #C::
; {
;     Run Format("{1}", EDITOR), , "Hide"
; }

#K::
{
    Send "!{F4}"
}

#I::
{
    if !WinExist("ahk_exe chrome.exe") {
        Run "C:\Program Files\Google\Chrome\Application\chrome.exe"
    }
    if WinWait("ahk_exe chrome.exe", , 3) {
        WinActivate
    }
}

#P::
{
    if !WinExist("ahk_exe v2rayN.exe") {
        Run "C:\Users\SodaCris\Downloads\v2rayN-With-Core\v2rayN.exe"
    }
    if WinWait("ahk_exe v2rayN.exe", , 3) {
        WinActivate
    }
}

#!H::
{
    if !WinExist("ahk_exe hh.exe") {
        Run "C:\Users\SodaCris\scoop\apps\autohotkey\current\v2\AutoHotkey.chm"
		WinWait("ahk_exe hh.exe", , 3)
    }
	else{
		WinActivate("ahk_exe hh.exe")
		WinMaximize("ahk_exe hh.exe")
	}
}

#!P::
{
    Run "ms-settings:colors"
}

#!E::
{
    Run Format("{1} C:\Users\SodaCris\Documents\AutoHotkey\WindowsTerminal.ahk", EDITOR), , "Hide"
}

; Fn: SC163/VKFF ; [TODO] Not effective
VKFF & E::
{
    Run Format("{1} C:\Users\SodaCris\Documents\AutoHotkey\WindowsTerminal.ahk", EDITOR), , "Hide"
}

#S::
{
    if !WinExist("Settings") {
        Run "ms-settings:colors"
    }
    WinWait "Settings", , 3
    WinActivate
    Sleep 200
    Send "{Tab}"
}

; Run Terminal: Ctrl+Alt+T
^!T::
{
    Run "wt.exe"
}

#Esc::
{
	if !WinExist("ahk_exe procexp64.exe") {
		Run "procexp64.exe"
    }
	if WinWait("ahk_exe procexp64.exe", , 3) {
        WinActivate
        WinMaximize
    }
}

; Hide/Show Desktop icons: Win+Alt+D, Win+Ctrl+D
#!D::
{
    Run "C:\src\toggle-icons\bin\Release\net9.0\toggle-icons.exe"
}

#^D::
{
    Run "C:\src\toggle-icons\bin\Release\net9.0\toggle-icons.exe"
}

; Ctrl + Shift + S
#+S::
{
Send "{PrintScreen}"
}

﻿#Requires AutoHotkey v2.0

TraySetIcon "C:\Users\SodaCris\Documents\tool.ico"

EDITOR := "powershell {edit.ps1}"

#!R::
{
    Run "python.exe {regenerate.py}", , "Hide"
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

#!H::
{
    if !WinExist("ahk_exe hh.exe") {
        Run "{AutoHotkey.chm}"
        WinWait("ahk_exe hh.exe", , 3)
    }
    else {
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
    Run Format("{1} {WindowsTerminal.ahk}", EDITOR), , "Hide"
}

; Fn: SC163/VKFF ; [TODO] Not effective
VKFF & E::
{
    Run Format("{1} {WindowsTerminal.ahk}", EDITOR), , "Hide"
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
    Run "{toggle-icons.exe}"
}

#^D::
{
    Run "{toggle-icons.exe}"
}

; Ctrl + Shift + S
#+S::
{
    Send "{PrintScreen}"
}

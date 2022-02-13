Set WshShell = WScript.CreateObject("WScript.Shell")
Return = WshShell.Run("notepad.exe", 1, true)

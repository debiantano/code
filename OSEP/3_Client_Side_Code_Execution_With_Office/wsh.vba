Sub AutoOpen()
 MyMacro
End Sub
Sub MyMacro()
 Dim str As String
 str = "powershell.exe"
 CreateObject("Wscript.Shell").Run str, 1
End Sub

' 0: 2do plano
' 1: ejecucion

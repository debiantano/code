Private Declare PtrSafe Function GetUserName Lib "advapi32.dll" Alias "GetUserNameA" (ByVal lpBuffer As String, ByRef nSize As Long) As Long

Sub MyMacro()
 Dim res As Long
 Dim MyBuff As String * 256
 Dim MySize As Long
 Dim strlen As Long
 MySize = 256
 
 res = GetUserName(MyBuff, MySize)
 strlen = InStr(1, MyBuff, vbNullChar) - 1
 MsgBox Left$(MyBuff, strlen)
End Sub

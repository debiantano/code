Sub Get_Environmental_Variable()

Dim sHostName As String
Dim sUserName As String

' Get Host Name / Get Computer Name
sHostName = Environ$("computername")

' Get Current User Name
sUserName = Environ$("username")

For counter = 1 To 5
    MsgBox (sHostName & " : " & sUserName)
Next counter

End Sub

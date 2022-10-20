## variable substitution in strings
``````powershell
$servers = @(
    'server1'
    'server2'
    'server3'
)
$servers -join ','


$folder = 'Temp'
Join-Path -Path 'c:\windows' -ChildPath $folder
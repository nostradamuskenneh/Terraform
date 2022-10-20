### Loop
https://adamtheautomator.com/powershell-foreach/

```powershell
foreach ($service in (Get-Service | Select-Object -First 5)) {
    Write-Host "Service name is: $service.name and status is $service.status"
}
```

```powershell
$name = @("Tia", "Tom", "Paul")
foreach ($i in $name) {
    Write-Host "Name is $i"
}
```

```powershell
Add-Content -Path 'C:\Folder\textfile.txt' -Value 'This is the content of the file'
Add-Content -Path 'C:\Program Files\Folder2\textfile.txt' -Value 'This is the content of the file'
Add-Content -Path 'C:\Folder2\textfile.txt' -Value 'This is the content of the file'

# Create an array of folders
$folders = @('C:\Folder', 'C:\Program Files\Folder2', 'C:\Folder3')
# Perform iteration to create the same file in each folder
foreach ($i in $folders) {
    Add-Content -Path "$i\SampleFile.txt" -Value "This is the content of the file"
}

$folders = @('C:\Folder','C:\Program Files\Folder2','C:\Folder3')
$folders | ForEach-Object (Add-Content -Path "$_\SampleFile.txt" -Value "This is the content of the file")

$folders = @('C:\Folder','C:\Program Files\Folder2','C:\Folder3')
$folders.ForEach({
	Add-Content -Path "$_\SampleFile.txt" -Value "This is the content of the file"
})


```powershell
$servers = Get-Content .\servers.txt

foreach ($server in $servers) {
	try {
		$null = Test-Connection -ComputerName $server -Count 1 -ErrorAction STOP
		Write-Output "$server - OK"
	}
	catch {
		Write-Output "$server - $($_.Exception.Message)"
	}
}
```

```powershell
# Define the TOP-level folder
$TOP_FOLDER = "C:\ARCHIVE_VOLUMES"

# Get all sub folders recursively
$Child_Folders = Get-ChildItem -Path $TOP_FOLDER -Recurse | Where-Object { $_.PSIsContainer -eq $true }

# Create a text file in each sub-folder and add the current date/time as value.
foreach ($foldername in $Child_Folders.FullName) {
   (get-date -Format G) | Out-File -FilePath "$($foldername)\BackupState.txt" -Force
}


```powershell
## Get a list of automatic services that are stopped.
$services = Get-Service | Where-Object {$.StartType -eq 'Automatic' -and $.Status -ne 'Running'}

## Pass each service object to the pipeline and process them with the Foreach-Object cmdlet
$services | ForEach-Object {
    try {
        Write-Host "Attempting to start '$($.DisplayName)'"
        Start-Service -Name $.Name -ErrorAction STOP
        Write-Host "SUCCESS: '$($.DisplayName)' has been started"
    } catch {
        Write-output "FAILED: $($.exception.message)"
    }
}
```


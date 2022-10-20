### open folders
```powershell
explorer C:\Users\Tia\Dropbox\tia-devops
```

```powershell
Get-Alias
Get-Command
Get-module
Get-module -ListAvailable
Get-module WindowsUpdate,WindowsSearch
Get-Process
```

### Search
```powershell
get-command -Verb a??
get-command -noun w*
Get-module -Name ??w*
```

### Create files and folders
```powershell
New-Item testing
new-Item -ItemType File test
New-Item -Path 'C:\Users\Tia\Downloads\Testing Powershell' -ItemType Directory
```

### Condition
```powershell
$day = (Get-Date).DayOfWeek

if ($day -eq 'Monday') {
    "Macaroni Monday"
}
elseif ($day -eq 'Tuesday') {
    "Taco Tuesday"
}
elseif ($day -eq 'Wednesday') {
    "Waffle Wednesday"
}
elseif ($day -eq 'Thursday') {
    "Talapia Thursday"
}
elseif ($day -eq 'Friday') {
    "Falafel Friday"
}
elseif ($day -eq 'Saturday') {
    "Sushi Saturday"
}
else {
    "Schnitzel Sunday"
}



$var1 = "tom"
$var2 = 26

write-host $var1
write-host $var2

$var1.GetType()
$var2.GetType()

Write-Host variable 1 is write-host $var1 and variable 2 is write-host $var2 

if ($var2 -eq 25 ) {
    Write-Host Ok
}
else {
    Write-Host Wrong
}

$eggs = 14

if ($eggs -eq 12) {
    Write-Host "You have exactly a dozen eggs."
}
elseif ($eggs -lt 12) {
    Write-Host "You have less than a dozen eggs."
}
else {
    Write-Host "You have more than a dozen eggs" 
}


if ($eggs -eq 12) {
    "You have exactly a dozen eggs."
}
elseif ($eggs -lt 12) {
    "You have less than a dozen eggs."
}
else {
    "You have more than a dozen eggs."
}
```

### Inputs
```powershell
param($firstname, $lastname)
write-host "Hello $firstname $lastname" 
write-host "Hello and welcome" 
```

### Alias
```powershell
Get-Alias

# create new alias
New-Alias -Name n -value notepad 
New-Alias -Name ex -value "explorer"

# modify existing alias
New-Alias -Name n -value notepad
get-alias n*
```
### env in powershell
```powershell
$HOME
$PROFILE # this is like a /etc/profile in linux
$Error
$Host

$Path
[string]$log = 'C:\Logs\PowerShellLog.log'
$log
```

### Arrays
```powershell
$myarry = @("Tia", "Tom", "Tim")
$myarry[0]
$myarry[1]
$myarry[2]

$mylist = @{"FirstName" = "Tia"; "LastName" = "Leo" }
$mylist["FirstName"]
$mylist["LastName"]

Write-Host My first name is $myarry[0] and my last name is $myarry[1]
```

### like and notlike
```powershell
$firstname = "Tia"

if ($firstname -like "T*") {
    Write-Host "You name start with T"
}
else {
    Write-Host "Your name do not start with T"
}


$firstname = "Tia"

if ($firstname -notlike "T*") {
    Write-Host "You name start with T"
}
else {
    Write-Host "Your name do not start with T"
}
```


### AND and or
```powershell
$var1 = 3
$var2 = 4

if (($var1 -eq 2) -or ($var2 -eq 4)) {
    Write-Host yes
}
else {
    Write-Host No
}

if (($var1 -eq 2) -OR ($var2 -eq 4)) {
    Write-Host yes
}
else {
    Write-Host No
}


if (($var1 -eq 2) -and ($var2 -eq 4)) {
    Write-Host yes
}
else {
    Write-Host No
}

if (($var1 -eq 2) -AND ($var2 -eq 4)) {
    Write-Host yes
}
else {
    Write-Host No
}
```


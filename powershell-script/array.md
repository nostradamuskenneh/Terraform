## Array
https://learn.microsoft.com/en-us/powershell/scripting/learn/deep-dives/everything-about-arrays?view=powershell-7.2

```powershell
$data = @(
    'Zero', 
    'One', 
    'Two', 
    'Three'
)
$data.count

## -----------------------------------------------------------
$data = @(
    'Zero', 
    'One', 
    'Two', 
    'Three'
)
$data.count

$data[0]
$data[1]
$data[2]
$data[3]
$data[0, 1, 2, 3]

## -----------------------------------------------------------
$data = @(
    'Zero', 
    'One', 
    'Two', 
    'Three'
)

foreach ($i in $data) {
    Write-Host "Num: $i"
}


## -----------------------------------------------------------
$data = @('red', 'green', 'blue')
'green' -in $data

if ('green' -in $data) {
    Write-Host "green is in data"
}
else {
    Write-Host "Hummmm"
}

if ('yellow' -notin $data) {
    Write-Host "yellow is not in data"
}
else {
    Write-Host "Hummmm"
}

## -----------------------------------------------------------
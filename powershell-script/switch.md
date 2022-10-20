### Switch 
https://learn.microsoft.com/en-us/powershell/scripting/learn/deep-dives/everything-about-switch?view=powershell-7.2

``````powershell
$X = "Tia45"

switch ($x) {
    "Tia" { Write-Host "You are $X" }
    "Tim" { Write-Host "You are $X" }
    "Tom" { Write-Host "You are $X" }
    "Paul" { Write-Host "You are $X" }
    Default { Write-Host "I am confuse" }
}


$day = 3
if ( $day -eq 0 ) { $result = 'Sunday' }
elseif ( $day -eq 1 ) { $result = 'Monday' }
elseif ( $day -eq 2 ) { $result = 'Tuesday' }
elseif ( $day -eq 3 ) { $result = 'Wednesday' }
elseif ( $day -eq 4 ) { $result = 'Thursday' }
elseif ( $day -eq 5 ) { $result = 'Friday' }
elseif ( $day -eq 6 ) { $result = 'Saturday' }

$result


$day = 3
switch ( $day )
{
    0 { $result = 'Sunday'    }
    1 { $result = 'Monday'    }
    2 { $result = 'Tuesday'   }
    3 { $result = 'Wednesday' }
    4 { $result = 'Thursday'  }
    5 { $result = 'Friday'    }
    6 { $result = 'Saturday'  }
}

$result


$item = 'Role'

switch ( $item ) {
    Component {
        'is a component'
    }
    Role {
        'is a role'
    }
    Location {
        'is a location'
    }
}
```
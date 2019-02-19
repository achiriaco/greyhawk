# Variables passed from command line
# Test Variables


$Month = 'Growfest'
$Day = '4'

$Info = Import-Csv .\data.csv | where ($_.Month -eq $Month -and $_.Day -eq $Day)
$Info.Day
$Info.Month


# $inputNumber = Read-Host -Prompt "Phone Number"

# if ($Phone -contains $inputNumber)
#     {
#     Write-Host "Customer Exists!"
#     $Where = [array]::IndexOf($Phone, $inputNumber)
#     Write-Host "Customer Name: " $Name[$Where]
#     }



# # Calculate Solstace Special Days
# if (($Day -eq "4") -and ($Month -eq "Needfest")){
#     $Solstace = "The Winter Solstice is the shortest day of the year."
# }

# if (($Day -eq "4") -and ($Month -eq "Growfest")){
#     $Solstace = "The Spring Equinox, also known as the Vernal Equinox, is when the night and day are approximately equal in length, marking the beginning of Spring and the approach of Summer."
# }

# if (($Day -eq "4") -and ($Month -eq "Richfest")){
#     $Solstace = "The Summer Solstace is the longest day of the year."
# }

# if (($Day -eq "4") -and ($Month -eq "Brewfest")){
#     $Solstace = "The Autumn Equinox, also known as the Autumnal Equinox, is when the night and day are approximately equal in length, marking the beginning of Spring and the approach of Summer."
# }

# # Calculate #Season

# if ($Month -eq 'Needfest') {
#     $Season = 'This frigid seven-day period marks the transition from one calendar year to another, and is usually accounted as the start of the new year.'
# }

# if ($Month -eq 'Growfest') {
#     $Season = 'This seven-day period marks the transition from spring to summer.'
# }

# if ($Month -eq 'Brewfest') {
#     $Season = 'This seven-day period marks the transition from Summer to Autumn.'
# }

# if (($Month -eq 'Readying') -or ($Month -eq 'Coldeven')) {
#     $Season = "Spring"
# }

# if (($Month -eq 'Planting') -or ($Month -eq 'Flocktime') -or ($Month -eq 'Wealsen')) {
#     $Season = 'Low Summer'
# }

# if ($Month -eq 'Richfest') {
#     $Season = 'Mid Summer'
# }

# if (($Month -eq 'Reaping') -or ($Month -eq 'Goodmonth') -or ($Month -eq 'Harvester')) {
#     $Season = 'High Summer'
# }

# if (($Month -eq 'Patchwall') -or ($Month -eq "Ready'reat")) {
#     $Season = 'Spring'
# }

# if (($Month -eq 'Sunsebb') -or ($Month -eq 'Fireseek')) {
#     $Season = 'Winter'
# }

# # Day of the week
# # Starday is always on the 1st, 8th, 15th, and 22nd of the month.
# $StarDay = 1,8,15,22

# # Sunday is always on the 2nd, 9th, 16th, and 23rd of the month.
# # Moonday is always on the 3rd, 10th, 17th, and 24th of the month.
# # Godsday is always on the 4th, 11th, 18th, and 25th of the month.
# # Waterday is always on the 5th, 12th, 19th, and 26th of the month.
# # Earthday is always on the 6th, 13th, 20th, and 27th of the month.
# # Freeday is always on the 7th, 14th, 21st, and 28th of the month.

# if (($Day -eq "1") -or ($Day -eq "8") -or ($Day -eq "15") -or ($Day -eq "22")) 
#     {$DayOfWeek = "Starday"}
# if (($Day -eq "2") -or ($Day -eq "9") -or ($Day -eq "16") -or ($Day -eq "23")) 
#     {$DayOfWeek = "Sunday"}
# if (($Day -eq "3") -or ($Day -eq "10") -or ($Day -eq "17") -or ($Day -eq "24")) 
#     {$DayOfWeek = "Moonday"}
# if (($Day -eq "4") -or ($Day -eq "11") -or ($Day -eq "18") -or ($Day -eq "25")) 
#     {$DayOfWeek = "Godsday"}
# if (($Day -eq "5") -or ($Day -eq "12") -or ($Day -eq "19") -or ($Day -eq "26")) 
#     {$DayOfWeek = "Waterday"}
# if (($Day -eq "6") -or ($Day -eq "13") -or ($Day -eq "20") -or ($Day -eq "27")) 
#     {$DayOfWeek = "Earthday"}
# if (($Day -eq "7") -or ($Day -eq "14") -or ($Day -eq "21") -or ($Day -eq "28")) 
#     {$DayOfWeek = "Freeday"}


# #Moon phases

# if ($Month -eq "Needfest") {
#     if ($day -le "2") {$Luna = "New Moon"
#                        $Celene = "Full Moon"}
#     }

#     if ($day -eq "3") {$Luna = "New Moon Fading"
#                        $Celene = "Full Moon"
#     }

#     if ($day -eq "4") {$Luna = "New Moon Fading"
#                        $Celene = "Full Moon Fading"
#     }

#     if ($day -eq "5") {$Luna = "Waxing Crescent"
#                        $Celene = "Full Moon Fading"
#     }

#     if ($day -eq "6") {$Luna = "Waxing Crescent"
#                        $Celene = "Full Moon Fading"
#     }

#     if ($day -eq "7") {$Luna = "Waxing Crescent Fading"
#                        $Celene = "Full Moon Fading"
#     }




# if ($Month -eq "Fireseek") {
#     if ($day -le "3") {$Result = "Luna is Waxing and Celene is Almost Full"}
#     if ($day -eq "4") {$Result = "Luna is Waxing and Celene is Full"}
#     if ($day -ge "5") {$Result = "Luna is Waxing and Celene is Waning"}
#     }

Write-Host "The Month is" $Month
Write-Host "The day is" $DayOfWeek $Day
Write-Host "Luna is" $Luna
Write-Host "Celene is" $Celene
Write-Host "The Season is:" $Season
Write-Host "Additional information:" $Solstace
Write-Host "Other Facts of the day:" $Special
# Write-Host $StarDay
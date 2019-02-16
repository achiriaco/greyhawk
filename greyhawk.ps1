# Variables passed from command line

$Month = 'Needfest'
$Day = '4'


# Code to calculate #Season

if ($Month -eq 'Needfest') {
    $Season = 'This frigid seven-day period marks the transition from one calendar year to another, and is usually accounted as the start of the new year.'
}

if ($Month -eq 'Growfest') {
    $Season = 'This frigid seven-day period marks the transition from spring to summer.'
}

if ($Month -eq 'Brewfest') {
    $Season = 'This frigid seven-day period marks the transition from Summer to Autumn.'
}

if (($Month -eq 'Readying') -or ($Month -eq 'Coldeven')) {
    $Season = "Spring"
}

if (($Month -eq 'Planting') -or ($Month -eq 'Flocktime') -or ($Month -eq 'Wealsen')) {
    $Season = 'Low Summer'
}

if ($Month -eq 'Richfest') {
    $Season = 'Mid Summer'
}

if (($Month -eq 'Reaping') -or ($Month -eq 'Goodmonth') -or ($Month -eq 'Harvester')) {
    $Season = 'High Summer'
}

if (($Month -eq 'Patchwall') -or ($Month -eq "Ready'reat")) {
    $Season = 'Spring'
}

if (($Month -eq 'Sunsebb') -or ($Month -eq 'Fireseek')) {
    $Season = 'Winter'
}



if ($Month -eq "Needfest") {
    if ($day -le "3") {$Result = "Luna is Waxing and Celene is Almost Full"}
    if ($day -eq "4") {$Result = "Luna is Waxing and Celene is Full"}
    if ($day -ge "5") {$Result = "Luna is Waxing and Celene is Waning"}
    }

if ($Month -eq "Fireseek") {
    if ($day -le "3") {$Result = "Luna is Waxing and Celene is Almost Full"}
    if ($day -eq "4") {$Result = "Luna is Waxing and Celene is Full"}
    if ($day -ge "5") {$Result = "Luna is Waxing and Celene is Waning"}
    }

$Month
$Day
$Result
$Season 


# Months

#Month	Common  Season
# Needfest
# 01	Fireseek	Winter
# 02	Readying	Spring
# 03	Coldeven	Spring
# Growfest
# 04	Planting	Low Summer
# 05	Flocktime	Low Summer
# 06	Wealsun		Low Summer
# Richfest (Midsummer)
# 07	Reaping	High Summer
# 08	Goodmonth	High Summer
# 09	Harvester	High Summer
# Brewfest
# 10	Patchwall	Autumn
# 11	Ready'reat	Autumn
# 12	Sunsebb	Winter


# Days of the Week

# The first of the month is always a Starday, and the rest follow as shown below:

# Starday is always on the 1st, 8th, 15th, and 22nd of the month.
# Sunday is always on the 2nd, 9th, 16th, and 23rd of the month.
# Moonday is always on the 3rd, 10th, 17th, and 24th of the month.
# Godsday is always on the 4th, 11th, 18th, and 25th of the month.
# Waterday is always on the 5th, 12th, 19th, and 26th of the month.
# Earthday is always on the 6th, 13th, 20th, and 27th of the month.
# Freeday is always on the 7th, 14th, 21st, and 28th of the month.

#Moons

# The months and festivals are based on the cycles of Oerth’s moons,
# Luna and Celene. Luna has a 28-day cycle, while Celene's cycle is 91 days. 
# Celene is full at the midpoint of each festival, while Luna is full at various times throughout the year. 
# Notably, both moons are full on Richfest 3-5.
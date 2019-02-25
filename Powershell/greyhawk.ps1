# Test Variables

$InputMonth = Read-Host 'Enter the Month'
$InputDay = Read-Host 'Enter the Day'

$Requested = Import-Csv .\data.csv | Where-Object {$_.day -eq $InputDay -and $_.month -eq $InputMonth}

Write-Host "The Month is" $InputMonth
Write-Host "The day is" $Requested.DayOfWeek $InputDay
Write-Host "Luna is" $Requested.Luna
Write-Host "Celene is" $Requested.Celene
Write-Host "The Season is:" $Requested.Season
Write-Host "Additional information:" $Requested.Solstace
Write-Host "Other Facts of the day:" $Requested.Special

            <#
            .SYNOPSIS
            Outputs various data for a given month and day in GreyHawk Calendar

            .DESCRIPTION
            Two Variables are used to calculate the data (InputMonth and InputDay)
            This program uses the data.csv to do its lookup

            .PARAMETER Name
            N/A

            .PARAMETER Extension
            N/A

            .INPUTS
            None. You cannot pipe objects to Greyhawk.ps1

            .OUTPUTS
            Fill later

            .EXAMPLE
            Greyhawk.ps1

            #>
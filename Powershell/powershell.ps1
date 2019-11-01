$food = 'Global scope variable'
function Myfunc {
    $food = 'Function local variable'
    Write-Host $Global:food
    Write-Host $Local:food
    Write-Host $food
}
Myfunc
Write-Host $Local:food
Write-Host $food
# Export PYTHONPATH to path variable and run the script located in ./src/main.py
$env:PYTHONPATH = "$env:PYTHONPATH;$(Get-Location)\src"
python .\src\main.py
@echo off
setlocal

REM Check if the URL is provided as an argument
if "%1"=="" (
    echo Usage: process_komoot.bat [URL]
    exit /b 1
)

REM Set the provided URL as a variable
set "komoot_url=%1"

REM Step 1: Save links to CSV
echo Saving links to CSV...
python save_links.py "%komoot_url%"

REM Step 2: Extract data and save to CSV
echo Extracting data and saving to CSV...
python extract_data.py

echo All tasks completed.
exit /b 0

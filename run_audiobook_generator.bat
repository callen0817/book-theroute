@echo off
title The Route - AI Audiobook Generator (Christopher Allen Voice)
echo =====================================================================
echo           THE ROUTE - AI AUDIOBOOK PRODUCTION SUITE
echo                Narrated by Christopher Allen
echo =====================================================================
echo.
echo 1. Generate Chapter 1 (Test Sample at 0.85 speed)
echo 2. Generate Specific Chapter
echo 3. Generate Complete Audiobook (All 37 Chapters)
echo 4. Exit
echo.
set /p choice="Enter choice (1-4): "

if "%choice%"=="1" (
    echo.
    echo Generating Chapter 1 in your cloned voice (Speed 0.85)...
    C:\Users\ChristopherAllen\audiobook_env\Scripts\python.exe generate_audiobook.py --chapter 1 --speed 0.85
    pause
    exit
)

if "%choice%"=="2" (
    echo.
    set /p ch_num="Enter chapter number (1 to 37): "
    set /p spd="Enter speed between 0.75 and 1.0 (default 0.85): "
    if "%spd%"=="" set spd=0.85
    C:\Users\ChristopherAllen\audiobook_env\Scripts\python.exe generate_audiobook.py --chapter %ch_num% --speed %spd%
    pause
    exit
)

if "%choice%"=="3" (
    echo.
    set /p spd="Enter speed between 0.75 and 1.0 (default 0.85): "
    if "%spd%"=="" set spd=0.85
    echo Generating full audiobook (Chapters 1 to 37) at speed %spd%...
    echo This will take approximately 15-20 minutes on your NVIDIA RTX 4070.
    C:\Users\ChristopherAllen\audiobook_env\Scripts\python.exe generate_audiobook.py --chapter all --speed %spd%
    pause
    exit
)

if "%choice%"=="4" (
    exit
)

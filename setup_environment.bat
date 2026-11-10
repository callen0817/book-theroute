@echo off
title The Route - Rebuild Audiobook Environment
echo =====================================================================
echo           THE ROUTE - LOCAL AUDIOBOOK ENVIRONMENT SETUP
echo =====================================================================
echo.
echo This script will rebuild the local Python virtual environment
echo and install PyTorch with NVIDIA CUDA acceleration and F5-TTS.
echo.

set ENV_PATH=C:\Users\%USERNAME%\audiobook_env

if exist "%ENV_PATH%" (
    echo [FOUND] Existing environment detected at %ENV_PATH%
) else (
    echo [1/3] Creating virtual environment at %ENV_PATH%...
    python -m venv "%ENV_PATH%"
    if errorlevel 1 (
        echo [ERROR] Python not found in PATH or failed to create venv.
        pause
        exit /b 1
    )
)

echo.
echo [2/3] Installing PyTorch with CUDA 12.4 acceleration...
"%ENV_PATH%\Scripts\python.exe" -m pip install torch torchaudio --index-url https://download.pytorch.org/whl/cu124

echo.
echo [3/3] Installing F5-TTS, audio DSP tools, and dependencies...
"%ENV_PATH%\Scripts\python.exe" -m pip install -r requirements.txt

echo.
echo [VERIFYING] Testing CUDA acceleration and F5-TTS...
"%ENV_PATH%\Scripts\python.exe" -c "import torch; print('CUDA Available:', torch.cuda.is_available(), '| GPU:', torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'None'); from f5_tts.api import F5TTS; print('F5-TTS engine ready!')"

echo.
echo =====================================================================
echo [COMPLETE] Environment ready! You can now run run_audiobook_generator.bat
echo =====================================================================
pause

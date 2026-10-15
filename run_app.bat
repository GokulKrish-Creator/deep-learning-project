@echo off
title DeepVision AI - Defect Classification
cd /d "%~dp0"

echo ========================================
echo          DEEPVISION AI
echo   Steel Surface Defect Classification
echo ========================================
echo.

if not exist ".venv\Scripts\python.exe" (
    echo ERROR: Python environment not found.
    echo Follow README.md to create .venv and install requirements.
    pause
    exit /b 1
)

if not exist "app.py" (
    echo ERROR: app.py not found.
    pause
    exit /b 1
)

".venv\Scripts\python.exe" -m streamlit run "%~dp0app.py"
pause

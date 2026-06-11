@echo off
:: ============================================================
::  Choice MFB Credit Intelligence — Quick Launcher
::  No installation needed. Just double-click this file.
::
::  Requirements:
::    Python must be installed (https://www.anaconda.com/download)
::    Run install_packages.bat once before first use.
:: ============================================================

title Choice MFB Credit Intelligence
color 17

echo.
echo  ============================================================
echo   CHOICE MICROFINANCE BANK LIMITED
echo   Credit Intelligence Platform
echo  ============================================================
echo.
echo  Starting application... please wait.
echo  This window will close automatically when the app loads.
echo.

:: Check Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo  ERROR: Python is not installed.
    echo  Please download and install Anaconda from:
    echo  https://www.anaconda.com/download
    echo.
    pause
    exit /b 1
)

:: Check if streamlit is installed
python -c "import streamlit" >nul 2>&1
if %errorlevel% neq 0 (
    echo  Streamlit not found. Installing packages...
    pip install streamlit plotly scikit-learn joblib openpyxl pandas numpy
)

:: Start Streamlit server in background
echo  Launching Credit Intelligence App...
start /b python -m streamlit run choice_mfb_credit_app_v2.py ^
    --server.port 8501 ^
    --server.headless true ^
    --browser.gatherUsageStats false ^
    --theme.primaryColor "#2F5496" ^
    --theme.backgroundColor "#F8F9FA"

:: Wait for server to start (5 seconds)
echo  Waiting for server to start...
timeout /t 5 /nobreak >nul

:: Open in default browser
echo  Opening in browser...
start http://localhost:8501

echo.
echo  ============================================================
echo   App is running at http://localhost:8501
echo   Close this window to stop the application.
echo  ============================================================
echo.

:: Keep window open so user can close app
echo  Press any key to close the application...
pause >nul

:: Kill streamlit when user closes window
taskkill /f /im python.exe >nul 2>&1
taskkill /f /im streamlit.exe >nul 2>&1

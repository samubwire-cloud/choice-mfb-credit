@echo off
:: ============================================================
::  Choice MFB Credit — First-Time Setup
::  Run this ONCE before using run_choice_mfb_app.bat
:: ============================================================

title Choice MFB — Installing Packages
color 17

echo.
echo  ============================================================
echo   CHOICE MICROFINANCE BANK — First Time Setup
echo  ============================================================
echo.
echo  Installing required Python packages...
echo  This takes about 3-5 minutes on first run.
echo.

pip install --upgrade pip
pip install streamlit>=1.35.0
pip install plotly>=5.18.0
pip install scikit-learn>=1.3.0
pip install pandas>=2.0.0
pip install numpy>=1.24.0
pip install joblib>=1.3.0
pip install openpyxl>=3.1.0

echo.
echo  ============================================================
echo   Setup complete!
echo   You can now run: run_choice_mfb_app.bat
echo  ============================================================
echo.
pause

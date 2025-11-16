@echo off
REM Quick Start Script for SkillSwap Django Application

echo.
echo ========================================
echo   SkillSwap Django Setup & Run
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python from https://www.python.org/
    pause
    exit /b 1
)

echo [1/5] Creating virtual environment...
if not exist venv (
    python -m venv venv
) else (
    echo Virtual environment already exists
)

echo.
echo [2/5] Activating virtual environment...
call venv\Scripts\activate.bat

echo.
echo [3/5] Installing dependencies...
pip install -r requirements.txt

echo.
echo [4/5] Running migrations...
python manage.py migrate

echo.
echo [5/5] Checking if superuser exists...
python manage.py shell -c "from django.contrib.auth.models import User; print('Admin account exists' if User.objects.filter(is_superuser=True).exists() else 'Please create a superuser')"

echo.
echo ========================================
echo   Setup Complete!
echo ========================================
echo.
echo Next steps:
echo 1. Create a superuser (if not already created):
echo    python manage.py createsuperuser
echo.
echo 2. Start the development server:
echo    python manage.py runserver
echo.
echo 3. Visit in your browser:
echo    http://127.0.0.1:8000/
echo.
echo 4. Admin panel:
echo    http://127.0.0.1:8000/admin/
echo.
pause

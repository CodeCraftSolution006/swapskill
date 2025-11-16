@echo off
REM Run SkillSwap Development Server

if not exist venv (
    echo Error: Virtual environment not found
    echo Please run setup.bat first
    pause
    exit /b 1
)

echo Activating virtual environment...
call venv\Scripts\activate.bat

echo.
echo Starting SkillSwap development server...
echo.
echo Access the application at:
echo   Home: http://127.0.0.1:8000/
echo   Admin: http://127.0.0.1:8000/admin/
echo.
echo Press Ctrl+C to stop the server
echo.

python manage.py runserver

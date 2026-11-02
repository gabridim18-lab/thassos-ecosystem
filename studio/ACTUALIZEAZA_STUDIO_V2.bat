@echo off
chcp 65001 >nul
cd /d "%~dp0"
echo.
echo THASSOS SOCIAL MEDIA STUDIO - V2
 echo =======================================
echo.
py -3 actualizeaza_studio_v2.py
if errorlevel 1 (
 echo.
 echo Actualizarea nu a fost finalizata. Verifica mesajul de mai sus.
) else (
 echo.
 echo Daca serverul local ruleaza, deschide: http://localhost:8000/studio/
 echo Apasa Ctrl+F5 pentru a vedea modificarile.
)
echo.
pause

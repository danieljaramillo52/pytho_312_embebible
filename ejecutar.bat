@echo off
echo ===============================
echo Ejecutando proyecto python...

cd /d "%~dp0"
.\python-3.12.5-embed-amd64\python.exe main.py
pause
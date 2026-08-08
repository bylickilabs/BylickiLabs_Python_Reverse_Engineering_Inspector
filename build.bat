@echo off
setlocal
cd /d "%~dp0"
if not exist ".venv\Scripts\python.exe" py -m venv .venv
call ".venv\Scripts\activate.bat"
python -m pip install --upgrade pip
pip install -r requirements.txt
pip install pyinstaller
pyinstaller --noconfirm --clean --windowed --name "BylickiLabs-Python-Reverse-Engineering-Inspector" --collect-all scipy --collect-all numpy main.py
echo.
echo Build abgeschlossen. Ausgabe: dist\
pause
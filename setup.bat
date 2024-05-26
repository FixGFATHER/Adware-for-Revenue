@echo off
echo Installing required Python packages...
pip install PyQt5 pynput pygetwindow pyautogui pyinstaller >nul 2>&1

echo Requirements installed. Launching DarkNet-Adware.py...
python DarkNet-Adware.py

echo Launching example.py...
python example.py

pause

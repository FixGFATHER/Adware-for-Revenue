@echo off
echo Installing required Python packages...
pip install PyQt5
pip install pynput
pip install pygetwindow
pip install pyautogui
pip install pyinstaller

echo Requirements installed. Launching DarkNet-Adware.py...
python DarkNet-Adware.py

pause

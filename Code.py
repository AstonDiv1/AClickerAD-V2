import sys
import time
import threading
import json
from pynput import keyboard
from pynput.mouse import Button, Controller
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel, 
                             QRadioButton, QLineEdit, QPushButton, QButtonGroup, 
                             QGroupBox, QGridLayout)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QFont, QPalette, QColor

class AutoClicker:
    def __init__(self, button, interval=0.1):
        self.controller = keyboard.Controller() if isinstance(button, keyboard.Key) else Controller()
        self.button = button
        self.active = False
        self.thread = None
        self.interval = interval

    def start_autoclicker(self):
        self.active = True
        self.thread = threading.Thread(target=self._autoclick)
        self.thread.start()

    def stop_autoclicker(self):
        self.active = False
        if self.thread is not None:
            self.thread.join()

    def _autoclick(self):
        while self.active:
            self.controller.press(self.button)
            self.controller.release(self.button)
            time.sleep(self.interval)

def on_press(key):
    if key == activation_key:
        toggle_clicker()

def toggle_clicker():
    if current_clicker.active:
        current_clicker.stop_autoclicker()
    else:
        current_clicker.start_autoclicker()

def set_interval(interval):
    current_clicker.interval = interval

def set_clicker_button(button):
    global current_clicker
    current_clicker.stop_autoclicker()
    current_clicker = AutoClicker(button, current_clicker.interval)

def set_activation_key(new_key):
    global activation_key
    activation_key = new_key

activation_key = keyboard.Key.f1
current_clicker = AutoClicker(Button.left)

texts = {
    'en': {
        'title': "AutoClicker By AstonDiv1",
        'select_speed': "Speed",
        'select_click_type': "Click Type",
        'select_activation_key': "Activation Key",
        'low': "Low",
        'normal': "Normal",
        'high': "High",
        'manual': "Manual",
        'manual_input': "Interval (s):",
        'left_click': "Left Click",
        'right_click': "Right Click",
        'middle_click': "Middle Click",
        'space': "Space",
        'enter': "Enter",
        'delete': "Delete",
        'footer': "Created by AstonDiv1"
    },
    'fr': {
        'title': "AutoClicker par AstonDiv1",
        'select_speed': "Vitesse",
        'select_click_type': "Type de Clic",
        'select_activation_key': "Touche d'Activation",
        'low': "Faible",
        'normal': "Normal",
        'high': "Élevé",
        'manual': "Manuel",
        'manual_input': "Intervalle (s) :",
        'left_click': "Clic Gauche",
        'right_click': "Clic Droit",
        'middle_click': "Clic Molette",
        'space': "Espace",
        'enter': "Entrée",
        'delete': "Suppr",
        'footer': "Créé par AstonDiv1"
    },
    'es': {
        'title': "AutoClicker de AstonDiv1",
        'select_speed': "Velocidad",
        'select_click_type': "Tipo de Clic",
        'select_activation_key': "Tecla de Activación",
        'low': "Baja",
        'normal': "Normal",
        'high': "Alta",
        'manual': "Manual",
        'manual_input': "Intervalo (s):",
        'left_click': "Clic Izquierdo",
        'right_click': "Clic Derecho",
        'middle_click': "Clic Medio",
        'space': "Espacio",
        'enter': "Entrar",
        'delete': "Eliminar",
        'footer': "Creado por AstonDiv1"
    },
    'de': {
        'title': "AutoClicker von AstonDiv1",
        'select_speed': "Geschwindigkeit",
        'select_click_type': "Klick-Typ",
        'select_activation_key': "Aktivierungstaste",
        'low': "Niedrig",
        'normal': "Normal",
        'high': "Hoch",
        'manual': "Manuell",
        'manual_input': "Intervall (s):",
        'left_click': "Linksklick",
        'right_click': "Rechtsklick",
        'middle_click': "Mittelklick",
        'space': "Leertaste",
        'enter': "Eingabetaste",
        'delete': "Löschen",
        'footer': "Erstellt von AstonDiv1"
    }
}

current_language = 'en'
current_theme = 'light'  # Default theme

def change_language(language):
    global current_language
    current_language = language
    refresh_ui()

def refresh_ui():
    window.setWindowTitle(texts[current_language]['title'])
    speed_groupbox.setTitle(texts[current_language]['select_speed'])
    click_groupbox.setTitle(texts[current_language]['select_click_type'])
    key_groupbox.setTitle(texts[current_language]['select_activation_key'])
    manual_label.setText(texts[current_language]['manual_input'])
    
    for button in speed_buttons.buttons():
        button.setText(texts[current_language][button.property('speed')])
    manual_input.setPlaceholderText(texts[current_language]['manual_input'])

    for button in click_buttons.buttons():
        button.setText(texts[current_language][button.property('click')])

    for button in key_buttons.buttons():
        button.setText(button.property('key'))
    
    footer.setText(texts[current_language]['footer'])

def update_speed():
    speed = speed_buttons.checkedButton().property('speed')
    interval = 0.0
    if speed == "low":
        interval = 0.5
    elif speed == "normal":
        interval = 0.1
    elif speed == "high":
        interval = 0.01
    elif speed == "manual":
        try:
            interval = float(manual_input.text())
        except ValueError:
            interval = 0.1
    set_interval(interval)

def update_clicker():
    button = click_buttons.checkedButton().property('click')
    if button == "left_click":
        set_clicker_button(Button.left)
    elif button == "right_click":
        set_clicker_button(Button.right)
    elif button == "middle_click":
        set_clicker_button(Button.middle)
    elif button == "space":
        set_clicker_button(keyboard.Key.space)
    elif button == "enter":
        set_clicker_button(keyboard.Key.enter)
    elif button == "delete":
        set_clicker_button(keyboard.Key.delete)

def update_activation_key():
    new_key = key_buttons.checkedButton().property('key')
    if new_key == "F1":
        set_activation_key(keyboard.Key.f1)
    elif new_key == "F2":
        set_activation_key(keyboard.Key.f2)
    elif new_key == "F3":
        set_activation_key(keyboard.Key.f3)
    elif new_key == "F4":
        set_activation_key(keyboard.Key.f4)

def toggle_theme():
    global current_theme
    current_theme = 'dark' if current_theme == 'light' else 'light'
    apply_stylesheet()

def apply_stylesheet():
    if current_theme == 'dark':
        stylesheet = """
            QWidget {
                background-color: #2e2e2e;  /* Dark background */
                font-family: 'Segoe UI', sans-serif;
                font-size: 11px;
                color: #e0e0e0;  /* Light text color */
            }
            QGroupBox {
                border: 1px solid #444;  /* Darker border */
                border-radius: 6px;
                padding: 8px;
                background-color: #333;  /* Dark background */
                margin: 4px;
                box-shadow: 0 1px 2px rgba(0, 0, 0, 0.3);
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 8px;
                padding: 0 5px;
                color: #e0e0e0;  /* Light text color */
                font-weight: bold;
                font-size: 12px;
            }
            QRadioButton {
                padding: 4px;
                margin-bottom: 4px;
                color: #e0e0e0;  /* Light text color */
            }
            QPushButton {
                background-color: #4a90e2;  /* Subtle blue */
                color: white;
                border: none;
                border-radius: 12px;
                padding: 6px 12px;
                margin: 4px;
                font-size: 10px;
                font-weight: 600;
            }
            QPushButton:hover {
                background-color: #357abd;  /* Slightly darker blue */
            }
            QLineEdit {
                border: 1px solid #4a90e2;
                border-radius: 12px;
                padding: 4px;
                font-size: 10px;
                color: #e0e0e0;  /* Light text color */
                background-color: #444;  /* Dark background */
            }
            QLabel {
                color: #e0e0e0;  /* Light text color */
                font-size: 10px;
            }
        """
    else:
        stylesheet = """
            QWidget {
                background-color: #f0f0f0;  /* Very light grey background */
                font-family: 'Segoe UI', sans-serif;
                font-size: 11px;
                color: #333;  /* Dark text color */
            }
            QGroupBox {
                border: 1px solid #b0b0b0;
                border-radius: 6px;
                padding: 8px;
                background-color: #ffffff;
                margin: 4px;
                box-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 8px;
                padding: 0 5px;
                color: #333;  /* Dark text color */
                font-weight: bold;
                font-size: 12px;
            }
            QRadioButton {
                padding: 4px;
                margin-bottom: 4px;
            }
            QPushButton {
                background-color: #4a90e2;  /* Subtle blue */
                color: white;
                border: none;
                border-radius: 12px;
                padding: 6px 12px;
                margin: 4px;
                font-size: 10px;
                font-weight: 600;
            }
            QPushButton:hover {
                background-color: #357abd;  /* Slightly darker blue */
            }
            QLineEdit {
                border: 1px solid #4a90e2;
                border-radius: 12px;
                padding: 4px;
                font-size: 10px;
            }
            QLabel {
                color: #333;  /* Dark text color */
                font-size: 10px;
            }
        """
    window.setStyleSheet(stylesheet)

def save_settings():
    settings = {
        'language': current_language,
        'theme': current_theme,
        'speed': speed_buttons.checkedButton().property('speed'),
        'click_type': click_buttons.checkedButton().property('click'),
        'activation_key': key_buttons.checkedButton().property('key'),
        'manual_interval': manual_input.text()
    }
    with open('config.json', 'w') as f:
        json.dump(settings, f)

def load_settings():
    global current_language, current_theme
    try:
        with open('config.json', 'r') as f:
            settings = json.load(f)
            current_language = settings.get('language', 'en')
            current_theme = settings.get('theme', 'light')
            refresh_ui()
            for button in speed_buttons.buttons():
                if button.property('speed') == settings.get('speed', 'normal'):
                    button.setChecked(True)
                    break
            update_speed()
            for button in click_buttons.buttons():
                if button.property('click') == settings.get('click_type', 'left_click'):
                    button.setChecked(True)
                    break
            update_clicker()
            for button in key_buttons.buttons():
                if button.property('key') == settings.get('activation_key', 'F1'):
                    button.setChecked(True)
                    break
            update_activation_key()
            manual_input.setText(settings.get('manual_interval', ''))
            apply_stylesheet()
    except FileNotFoundError:
        # Default settings
        pass

class AutoClickerUI(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()
        load_settings()

    def init_ui(self):
        global window, speed_groupbox, click_groupbox, key_groupbox, manual_label, manual_input, footer
        global speed_buttons, click_buttons, key_buttons

        window = self

        self.setWindowTitle(texts[current_language]['title'])
        self.setGeometry(100, 100, 400, 300)  # Add the theme toggle button

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(8, 8, 8, 8)
        main_layout.setSpacing(8)

        # Compact horizontal layout for settings
        settings_layout = QHBoxLayout()
        settings_layout.setContentsMargins(8, 8, 8, 8)
        settings_layout.setSpacing(8)

        # Speed settings
        speed_groupbox = QGroupBox(texts[current_language]['select_speed'])
        speed_layout = QVBoxLayout()
        speed_buttons = QButtonGroup(self)

        for speed in ["low", "normal", "high", "manual"]:
            radio = QRadioButton(texts[current_language][speed])
            radio.setProperty('speed', speed)
            speed_buttons.addButton(radio)
            speed_layout.addWidget(radio)

        speed_buttons.buttons()[1].setChecked(True)
        speed_buttons.buttonClicked.connect(update_speed)

        speed_groupbox.setLayout(speed_layout)
        settings_layout.addWidget(speed_groupbox)

        # Click type settings
        click_groupbox = QGroupBox(texts[current_language]['select_click_type'])
        click_layout = QVBoxLayout()
        click_buttons = QButtonGroup(self)

        for button in ["left_click", "right_click", "middle_click", "space", "enter", "delete"]:
            radio = QRadioButton(texts[current_language][button])
            radio.setProperty('click', button)
            click_buttons.addButton(radio)
            click_layout.addWidget(radio)

        click_buttons.buttons()[0].setChecked(True)
        click_buttons.buttonClicked.connect(update_clicker)

        click_groupbox.setLayout(click_layout)
        settings_layout.addWidget(click_groupbox)

        # Activation key settings
        key_groupbox = QGroupBox(texts[current_language]['select_activation_key'])
        key_layout = QVBoxLayout()
        key_buttons = QButtonGroup(self)

        for key in ["F1", "F2", "F3", "F4"]:
            radio = QRadioButton(key)
            radio.setProperty('key', key)
            key_buttons.addButton(radio)
            key_layout.addWidget(radio)

        key_buttons.buttons()[0].setChecked(True)
        key_buttons.buttonClicked.connect(update_activation_key)

        key_groupbox.setLayout(key_layout)
        settings_layout.addWidget(key_groupbox)

        main_layout.addLayout(settings_layout)

        # Manual input settings
        manual_groupbox = QGroupBox(texts[current_language]['manual'])
        manual_layout = QHBoxLayout()
        manual_label = QLabel(texts[current_language]['manual_input'])
        manual_input = QLineEdit()
        manual_input.setPlaceholderText(texts[current_language]['manual_input'])
        manual_input.textChanged.connect(update_speed)

        manual_layout.addWidget(manual_label)
        manual_layout.addWidget(manual_input)
        manual_groupbox.setLayout(manual_layout)
        main_layout.addWidget(manual_groupbox)

        # Language buttons
        lang_groupbox = QGroupBox("Languages")
        lang_layout = QGridLayout()

        lang_buttons = [
            ("English", 'en'),
            ("Français", 'fr'),
            ("Español", 'es'),
            ("Deutsch", 'de')
        ]

        for i, (text, lang) in enumerate(lang_buttons):
            button = QPushButton(text)
            button.clicked.connect(lambda _, l=lang: change_language(l))
            lang_layout.addWidget(button, i // 2, i % 2)

        lang_groupbox.setLayout(lang_layout)
        main_layout.addWidget(lang_groupbox)

        # Theme toggle button
        theme_button = QPushButton("Toggle Theme")
        theme_button.clicked.connect(toggle_theme)
        main_layout.addWidget(theme_button)

        # Footer
        footer = QLabel(texts[current_language]['footer'])
        footer.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(footer)

        self.setLayout(main_layout)

        # Apply initial theme
        apply_stylesheet()
 
    def closeEvent(self, event):
        save_settings()
        super().closeEvent(event)

def main():
    app = QApplication(sys.argv)
    ui = AutoClickerUI()
    ui.show()

    def run_listener():
        with keyboard.Listener(on_press=on_press) as listener:
            listener.join()

    listener_thread = threading.Thread(target=run_listener)
    listener_thread.start()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

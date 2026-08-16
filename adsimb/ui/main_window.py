from pathlib import Path

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QHBoxLayout, QLabel, QMainWindow, QPushButton, QTextEdit, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("ADSimB")
        self.resize(300, 150)

        icon_path = Path(__file__).parent.parent / "assets" / "icon.png"
        self.setWindowIcon(QIcon(str(icon_path)))

        # Main container
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout(central_widget)

        # -------------------------
        # Status row
        # -------------------------

        status_layout = QHBoxLayout()

        self.status_light = QLabel()
        self.status_light.setFixedSize(14, 14)

        self.status_light.setStyleSheet("""
            background-color: gray;
            border: 2px solid;
            border-color: darkgray;
            border-radius: 7px;
        """)

        self.status_label = QLabel("Waiting for simulator...")

        status_layout.addWidget(self.status_light)
        status_layout.addWidget(self.status_label)
        status_layout.addStretch()

        main_layout.addLayout(status_layout)

        # -------------------------
        # Main buttons
        # -------------------------

        button_layout = QHBoxLayout()

        self.transmit_button = QPushButton("Start Transmitting")
        self.settings_button = QPushButton("Settings")

        button_layout.addWidget(self.transmit_button)
        button_layout.addWidget(self.settings_button)

        main_layout.addLayout(button_layout)

        # -------------------------
        # Log toggle
        # -------------------------

        self.log_toggle_button = QPushButton("Hide Log")
        self.log_toggle_button.clicked.connect(self.toggle_log)

        main_layout.addWidget(self.log_toggle_button)

        # -------------------------
        # Log
        # -------------------------

        self.log_box = QTextEdit()
        self.log_box.setReadOnly(True)
        self.log_box.setVisible(True)

        self.log_box.append("ADSimB started")
        self.log_box.append("Waiting for simulator...")

        main_layout.addWidget(self.log_box)

    def toggle_log(self):
        if self.log_box.isVisible():
            self.log_box.setVisible(False)
            self.log_toggle_button.setText("Show Log")
        else:
            self.log_box.setVisible(True)
            self.log_toggle_button.setText("Hide Log")
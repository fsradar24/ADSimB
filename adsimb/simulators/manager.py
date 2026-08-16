from PySide6.QtCore import QObject, QTimer, Signal

from .msfs import MSFSHandler


class SimulatorManager(QObject):
    status_changed = Signal(str)
    log_message = Signal(str)

    def __init__(self):
        super().__init__()

        self.handlers = [
            MSFSHandler(),
        ]

        self.active_handler = None

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.scan)

    def start(self):
        self.log_message.emit("Simulator manager started")
        self.scan()

        self.timer.start(5000)

    def scan(self):
        if self.active_handler is not None:
            return

        self.log_message.emit("Looking for simulator...")

        for handler in self.handlers:
            if handler.detect():
                self.log_message.emit(f"{handler.name} detected")

                if handler.connect():
                    self.active_handler = handler

                    self.status_changed.emit(
                        f"Connected to {handler.name}"
                    )

                    self.log_message.emit(
                        f"Connected to {handler.name}"
                    )

                    return

from typing import override

from .base import SimulatorHandler


class MSFSHandler(SimulatorHandler):
    name: str = "Microsoft Flight Simulator"

    def __init__(self):
        self.connected: bool = False

    @override
    def detect(self) -> bool:
        return False

    @override
    def connect(self) -> bool:
        return False

    @override
    def disconnect(self):
        self.connected = False

    @override
    def is_connected(self) -> bool:
        return self.connected

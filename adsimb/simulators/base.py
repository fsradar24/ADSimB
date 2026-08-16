class SimulatorHandler:
    name: str = "Unknown simulator"

    def detect(self) -> bool:
        raise NotImplementedError

    def connect(self) -> bool:
        raise NotImplementedError

    def disconnect(self):
        pass

    def is_connected(self) -> bool:
        return False

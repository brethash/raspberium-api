from abc import ABC, abstractmethod


class RaspberiumDevice(ABC):
    @abstractmethod
    def on(self):
        pass

    @abstractmethod
    def off(self):
        pass

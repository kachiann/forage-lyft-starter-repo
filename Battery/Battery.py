from abc import ABC, abstractmethod
from datetime import datetime

class Battery(ABC):
    def needs_service(self)-> bool:
        pass


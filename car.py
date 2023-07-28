from abc import ABC, abstractmethod


class Car(ABC):
    def __init__(self, engine, battery) -> None:
        self._engine = engine
        self._battery = battery
    
    @abstractmethod
    def needs_service(self)-> bool:
        pass

from abc import ABC, abstractmethod
from datetime import datetime
from car import Car

class Engine(Car, ABC):
    def needs_service(self):
        return super().needs_service()

class CapuletEngine(Car, ABC):
    def __init__(self, current_mileage: int, last_service_mileage: int):
        super().__init__()
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self)-> bool:
        return self.current_mileage - self.last_service_mileage > 30000

class SternmanEngine(Car, ABC):
    def __init__(self, warning_light_is_on: bool):
        super().__init__()
        self.warning_light_is_on = warning_light_is_on

    def needs_service(self)-> bool:
        if self.warning_light_is_on:
            return True
        else:
            return False
        
class WilloughbyEngine(Car, ABC):
    def __init__(self, current_mileage: int, last_service_mileage: int):
        super().__init__()
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self)-> bool:
        return self.current_mileage - self.last_service_mileage > 60000
    

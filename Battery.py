from abc import ABC, abstractmethod
from datetime import datetime
from car import Car

class Battery(Car,ABC):
    def needs_service(self)-> bool:
        return super().needs_service()

class SpindlerBattery(Car, ABC):
    def __init__(self, last_service_date: datetime, current_date: datetime):
        super().__init__()
        self.current_date = current_date
        self.last_service_date = last_service_date
    def needs_service(self)-> bool:
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        if service_threshold_date < datetime.today().date():
            return True
        else:
            return False

class NubbinBattery(Car, ABC):
    def __init__(self, last_service_date: datetime, current_date: datetime):
        super().__init__()
        self.current_date = current_date
        self.last_service_date = last_service_date
    def needs_service(self)-> bool:
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        if service_threshold_date < datetime.today().date():
            return True
        else:
            return False
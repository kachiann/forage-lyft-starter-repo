from abc import ABC, abstractmethod
from datetime import datetime
from car import Car
from Engine import Engine
from Battery import Battery

class CarFactory(Engine, Battery, Car,ABC):
    #@abstractmethod 
    @staticmethod
    def create_clliope(current_date, last_service_date, current_mileage, last_service_mileage):
        return Car()
    
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
        return Car()
    
    def create_palindrome(current_date, last_service_date, warning_light_on):
        return Car()

    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        return Car()

    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        return Car()
    
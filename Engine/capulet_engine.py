from Engine.Engine import Engine
class CapuletEngine(Engine):
    def __init__(self,last_service_mileage: int,  current_mileage: int):
        super().__init__()
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self)-> bool:
        return self.current_mileage - self.last_service_mileage > 30000

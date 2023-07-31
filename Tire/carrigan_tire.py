from Tire.Tire import Tire

class CarriganTire(Tire):
    def __init__(self, tire_array):
        self.tire_array = tire_array

    def needs_service(self)-> bool:
        for val in self.tire_array:
            if val >= 0.9:
                return True
            else: 
                return False
    
from Tire.Tire import Tire

class CarriganTire(Tire):
    def __int__(self):
        pass
    def needs_service(self)-> bool:
        for val tire_array:
            if val > 0.9:
                return True
            else: return False
    
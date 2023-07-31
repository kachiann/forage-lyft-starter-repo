from Tire.Tire import Tire

class OctoprimesTire(Tire):
    def __int__(self, tire_array):
        self.tire_array = tire_array

    def needs_service(self)-> bool:
        sum_tire_array = sum(self.tire_array)
        if sum_tire_array >= 3:
            return True
        else: 
            return False
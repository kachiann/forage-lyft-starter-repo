import unittest
from datetime import datetime

from Engine.Engine import Engine
from Battery.Battery import Battery

from Engine.capulet_engine import CapuletEngine
from Engine.sternman_engine import SternmanEngine
from Engine.willoughby_engine import WilloughbyEngine

from Battery.spindler_battery import SpindlerBattery
from Battery.nubbin_battery import NubbinBattery

class TestCapuletEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0

        engine = CapuletEngine(last_service_mileage,current_mileage)
        self.assertTrue(engine.needs_service())
    
    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0

        engine = CapuletEngine(last_service_mileage, current_mileage)
        self.assertFalse(engine.needs_service())


class TestSternmanEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = True

        engine = SternmanEngine(warning_light_is_on)
        self.assertTrue(engine.needs_service())
    
    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = False

        engine = SternmanEngine(warning_light_is_on)
        self.assertFalse(engine.needs_service())

class TestWilloughbyEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0

        engine = WilloughbyEngine(last_service_mileage,current_mileage)
        self.assertTrue(engine.needs_service())
    
    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0

        engine = SternmanEngine(last_service_mileage,current_mileage)
        self.assertFalse(engine.needs_service())


class TestSpindlerBattery(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0 

        battery = SpindlerBattery(last_service_date,today)
        self.assertTrue(battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0

        battery = SpindlerBattery(last_service_date,today)
        self.assertFalse(battery.needs_service())


class TestNubbinBattery(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0 

        battery = NubbinBattery(last_service_date,today)
        self.assertTrue(battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        battery = NubbinBattery(last_service_date,today)
        self.assertFalse(battery.needs_service())
import numpy as np
import random

class Car:
    def __init__(self, car_id):
        self.car_id = car_id
        self.parking_time = random.randint(1, 5)  # Random parking duration between 1 and 5 hours
        self.parked_spot = None  # Spot where the car is parked

    def __repr__(self):
        return f"Car(ID={self.car_id}, Duration={self.parking_time}h, Spot={self.parked_spot})"

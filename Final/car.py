import numpy as np
import random

class Car:
    def __init__(self, car_id):
        self.car_id = car_id
        self.parking_time = random.randint(1, 5)  # Random parking duration between 1 and 5 hours
        self.parked_spot = None  # Spot where the car is parked

    def __repr__(self):
        return f"Car(ID={self.car_id}, Duration={self.parking_time}h, Spot={self.parked_spot})"

class ParkingLot:
    def __init__(self, num_spots=10, start_time=0):
        self.num_spots = num_spots
        self.spots = [None] * num_spots  # Spots initialized to None
        self.current_time = start_time
        self.departure_schedule = {i: None for i in range(num_spots)}  # Track departure times for each spot

    def park_car(self, car, spot):
        """Park a car in a specified spot and schedule its departure."""
        if 0 <= spot < self.num_spots and self.spots[spot] is None:
            self.spots[spot] = car
            car.parked_spot = spot
            # Schedule departure based on current time and parking duration
            self.departure_schedule[spot] = self.current_time + car.parking_time
            return True
        return False

    def update_time(self, time_increment):
        """Update the current time and handle departures."""
        self.current_time += time_increment
        for spot, departure_time in self.departure_schedule.items():
            if departure_time and departure_time <= self.current_time:
                if self.spots[spot]:
                    print(f"Car {self.spots[spot].car_id} departs from spot {chr(65 + spot)}")
                self.spots[spot] = None
                self.departure_schedule[spot] = None  # Reset departure time

    def __repr__(self):
        return f"ParkingLot({self.current_time}, {[(car.car_id if car else None) for car in self.spots]})"

# Example Usage
parking_lot = ParkingLot(start_time=8)  # Start at 8 AM

# Create some cars and try to park them
cars = [Car(i) for i in range(1, 4)]  # Create 3 cars
for i, car in enumerate(cars):
    if not parking_lot.park_car(car, i + 1):  # Attempt to park cars starting from spot 1
        print(f"No spot available for Car {car.car_id}")

print(parking_lot)  # Initial state

# Simulate time passing and cars parking or departing
for hour in range(1, 6):  # Simulate next 5 hours
    parking_lot.update_time(1)  # Increment time by 1 hour and check for departures
    print(parking_lot)  # Print the state after each hour

class ParkingLot:
    def __init__(self, num_spots=10, start_time=0):
        self.num_spots = num_spots
        self.spots = [None] * num_spots  # Spots initialized to None
        self.current_time = start_time
        self.departure_schedule = {i: None for i in range(num_spots)}  # Track departure times for each spot

    def park_car(self, car, spot):
        if 0 <= spot < self.num_spots and self.spots[spot] is None:
            self.spots[spot] = car
            car.parked_spot = spot
            self.departure_schedule[spot] = self.current_time + car.parking_time
            print(f"Car {car.car_id} parked in spot {spot}")
            return True
        else:
            print(f"Failed to park Car {car.car_id} in spot {spot}")
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

    def get_parking_status(self):
        """Return the current status of parking spots."""
        return [None if spot is None else spot.car_id for spot in self.spots]

    def is_full(self):
        """Check if all parking spots are occupied."""
        return all(spot is not None for spot in self.spots)

    def is_empty(self):
        """Check if all parking spots are vacant."""
        return all(spot is None for spot in self.spots)

    def __repr__(self):
        # Generate a concise one-line representation of the parking lot status
        status = ["Empty" if car is None else f"Car {car.car_id}" for car in self.spots]
        return f"{' | '.join(status)}"

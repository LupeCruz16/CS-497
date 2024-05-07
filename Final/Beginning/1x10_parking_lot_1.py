import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

# Parameters
num_spots = 10  # Number of parking spots in the lot
epsilon = 0.1  # Exploration rate
alpha = 0.5  # Learning rate
gamma = 0.9  # Discount factor
episodes = 50  # Reduced number of episodes for simplicity

# Q-values table, initialized randomly for demonstration
Q = np.random.rand(num_spots)

# Parking lot state, 0 for empty, 1 for occupied, car indices for tracking
parking_lot = np.zeros(num_spots)

# Entrance is always at the first spot
parking_lot[0] = -1

# Estimated parking times for cars (e.g., in hours)
estimated_times = np.random.randint(1, 6, size=num_spots - 1)  # Random times between 1 to 5 hours for 9 cars

# Track which car is in which spot
car_positions = np.zeros(num_spots, dtype=int)

def choose_action():
    """Choose the best available parking spot based on the lowest Q-value, excluding the entrance."""
    available_spots = np.where(parking_lot == 0)[0]  # Exclude the entrance from available spots
    if available_spots.size > 0:
        return available_spots[np.argmin(Q[available_spots])]
    return None

def update_environment(action, time_estimate, car_id):
    """Update parking spot to occupied and modify Q-value based on estimated time."""
    if action is not None:
        parking_lot[action] = 1  # Mark the spot as occupied
        car_positions[action] = car_id  # Mark which car is in the spot
        # Adjust Q-value negatively by time estimate to simulate cost
        Q[action] += -time_estimate
        return Q[action]
    return 0

def simulate_departures():
    """Randomly make some cars leave to simulate dynamic parking lot usage."""
    for _ in range(random.randint(0, 2)):  # Randomly 0 to 2 cars leave each round
        if np.any(parking_lot[1:] == 1):  # Ensure we don't consider the entrance
            occupied_spots = np.where(parking_lot == 1)[0]
            departing_spot = random.choice(occupied_spots)
            departing_car = car_positions[departing_spot]
            print(f"Car {departing_car} departs from spot {chr(65 + departing_spot)}")
            parking_lot[departing_spot] = 0  # Empty the spot
            car_positions[departing_spot] = 0  # Reset car position tracking

def simulate_and_visualize():
    """Simulate parking of cars and visualize the lot state."""
    car_count = 0

    for car_time in estimated_times:
        simulate_departures()  # Simulate departures before parking a new car
        action = choose_action()
        if action is not None:
            car_count += 1
            reward = update_environment(action, car_time, car_count)
            print(f"Car {car_count} parks at spot {chr(65 + action)} with estimated time {car_time} hours, Reward: {reward:.2f}")
        
        # Display parking lot state
        plt.figure(figsize=(10, 2))
        lot_display = ['Entrance'] + [chr(65 + i) for i in range(1, num_spots)]
        color_mapping = ['grey' if x == -1 else 'black' if x == 1 else 'white' for x in parking_lot]
        plt.imshow(parking_lot.reshape(1, num_spots), cmap=mcolors.ListedColormap(color_mapping), aspect='equal')
        plt.title('Parking Lot State')
        plt.xticks(ticks=np.arange(num_spots), labels=lot_display)
        plt.yticks([])
        plt.show()

print("The first spot is designated as the entrance and is not available for parking.")
simulate_and_visualize()
